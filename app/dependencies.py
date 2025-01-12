from fastapi import Security, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_403_FORBIDDEN

from app.constants import API_KEY


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_api_key(api_key: str = Security(oauth2_scheme)):
    if api_key != API_KEY:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Forbidden")
