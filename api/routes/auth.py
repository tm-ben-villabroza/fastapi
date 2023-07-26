from db.models.user import UserModel
from db.types.user import UserBaseType, UserWithManagerType
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from db.operations import user as user_op

import firebase_admin
import pyrebase
import json
from firebase_admin import credentials, auth
from fastapi import Request, Response
from sqlalchemy.orm import Session
from fastapi import Depends
from db.database import get_db

# setup authentication and authorization
cred = credentials.Certificate("ben-and-ben-sandbox-_service_account_keys.json")
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open("firebase_config.json")))

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", include_in_schema=False)
async def signup(request: Request, db: Session = Depends(get_db)):
    req = await request.json()
    email = req["email"]
    password = req["password"]
    if email is None or password is None:
        raise HTTPException(
            detail={"message": "Error! Missing Email or Password"}, status_code=400
        )
    try:
        user = auth.create_user(email=email, password=password)
        user = user_op.create_user(db, user)
        return JSONResponse(
            content={
                "message": f"Successfully created user with email {user.email}",
                "user": UserWithManagerType.from_orm(user).dict(),
            },
            status_code=200,
        )

    except Exception as exception:
        raise HTTPException(
            detail={"message": f"Error Creating User: {str(exception)}"},
            status_code=400,
        )


@router.post("/login", include_in_schema=False)
async def login(response: Response, request: Request, db: Session = Depends(get_db)):
    req_json = await request.json()
    email = req_json["email"]
    password = req_json["password"]

    user = pb.auth().sign_in_with_email_and_password(email, password)
    jwt = user["idToken"]

    user = db.query(UserModel).filter_by(email=email).first()
    response = JSONResponse(
        content={
            "success": True,
            "user": UserWithManagerType.from_orm(user).dict(),
        },
        status_code=200,
    )
    response.set_cookie(
        key="token",
        value=jwt,
        secure=False,
        httponly=True,
        samesite="strict",
    )

    return response


@router.post("/is-token-valid", include_in_schema=False)
async def validate_token(request: Request):
    headers = request.headers
    try:
        jwt = headers.get("Authorization")
        print(f"jwt:{jwt}")
        user = auth.verify_id_token(jwt)
        return JSONResponse(content={"user_id": user["uid"]}, status_code=200)
    except Exception as exception:
        raise HTTPException(
            detail={
                "message": f"There was an error validating the token: {str(exception)}"
            },
            status_code=400,
        )
