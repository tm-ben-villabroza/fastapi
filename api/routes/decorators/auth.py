from functools import wraps
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
                    "message": f"This endpoint requires authentication. You are missing an Authorization header"
                },
                status_code=401,
            )

        try:
            auth.verify_id_token(token)
        except ExpiredIdTokenError:
            raise HTTPException(
                detail={
                    "message": "Your token is expired. Login again",
                    "action": "login",
                },
                status_code=400,
            )
        except Exception as exception:
            raise HTTPException(
                detail={
                    "message": f"There was an error validating the token: {str(exception)}"
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
