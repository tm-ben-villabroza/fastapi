from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

import firebase_admin
import pyrebase
import json
from firebase_admin import credentials, auth
from fastapi import Request, Response

# setup authentication and authorization
cred = credentials.Certificate("ben-and-ben-sandbox-_service_account_keys.json")
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open("firebase_config.json")))

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", include_in_schema=False)
async def signup(request: Request):
    req = await request.json()
    email = req["email"]
    password = req["password"]
    if email is None or password is None:
        raise HTTPException(
            detail={"message": "Error! Missing Email or Password"}, status_code=400
        )
    try:
        user = auth.create_user(email=email, password=password)
        return JSONResponse(
            content={
                "message": f"Successfully created user {user.uid}",
                "user_id": f"{user.uid}",
            },
            status_code=200,
        )
    except Exception as exception:
        raise HTTPException(
            detail={"message": f"Error Creating User: {str(exception)}"},
            status_code=400,
        )


@router.post("/login", include_in_schema=False)
async def login(response: Response, request: Request):
    req_json = await request.json()
    email = req_json["email"]
    password = req_json["password"]
    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        jwt = user["idToken"]
        response = JSONResponse(content={"success": True}, status_code=200)
        response.set_cookie(
            key="token",
            value=jwt,
            secure=False,
            httponly=True,
            samesite="strict",
        )

        return response
    except Exception as exception:
        raise HTTPException(
            detail={"message": f"There was an error logging in: {str(exception)}"},
            status_code=400,
        )


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
