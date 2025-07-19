import authlib
from fastapi import APIRouter, Depends, Request, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status
from secrets import token_urlsafe

from core.db import get_async_session, REDIS
from models.users import User


router = APIRouter()


# @router.post("/get-csrf-token")
# async def csrf_token(request: Request):
#     """
#     Endpoint to generate a CSRF token.
#     """
#     csrf_token = token_urlsafe(32)

#     response = JSONResponse(content={"csrf_token": csrf_token})
#     response.set_cookie(key="csrf_token", value=csrf_token, httponly=True, secure=True)
#     return response


@router.post("/login")
async def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint for user login.
    """
    session = await get_async_session()
    user = await User.authenticate(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {""}


@router.post("/2fa-verify")
async def two_factor_verify(request: Request):
    """
    Endpoint for verifying two-factor authentication.
    """
    pass


@router.get("/refresh")
async def refresh_token():
    """
    Endpoint to refresh user token.
    """
    pass
