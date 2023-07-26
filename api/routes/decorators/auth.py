from functools import wraps
from db.models.user import UserModel
from firebase_admin import auth
from firebase_admin.auth import ExpiredIdTokenError
from fastapi.exceptions import HTTPException


def require_authentication(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request = kwargs.get("request", None)
        if not request:
            raise HTTPException(
                detail={
                    "message": f"The endpoint must have the client 'request' as a parameter"
                },
                status_code=400,
            )

        token = request.cookies.get("token", None)
        if not token:
            raise HTTPException(
                detail={
                    "message": f"This endpoint requires authentication. You are missing an cookie called token."
                },
                status_code=401,
            )

        try:
            user_firebase = auth.verify_id_token(token)
            email_firebase = user_firebase["email"]

            db = kwargs.get("db", None)
            user = db.query(UserModel).filter_by(email=email_firebase).first()
            kwargs["user"] = user
        except ExpiredIdTokenError:
            raise HTTPException(
                detail={
                    "message": "Your token is expired. Login again",
                    "action": "login",
                },
                status_code=400,
            )

        return await func(*args, **kwargs)

        # make synchronous endpoints work
        # try:
        #     return await func(*args, **kwargs)
        # except TypeError:
        #     return func(*args, **kwargs)
        # except Exception as exception:
        #     raise HTTPException(
        #         detail={
        #             "message": f"There was an returning the inner fucntion: {str(exception)}"
        #         },
        #         status_code=400,
        #     )

    return wrapper
