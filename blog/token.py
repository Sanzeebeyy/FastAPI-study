from datetime import timedelta, datetime
from jose import jwt, JWTError
from .schemas import TokenData, Token

SECRET_KEY = "afc272d9efa4a8a16df8109486cd6a06223ee12fc71e0383a7648f8d743b57db"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict, expiry_delta: timedelta|None = None):
    to_encode = data.copy()
    if expiry_delta:
        expiry = datetime.utcnow()+expiry_delta
    else:
        expiry = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expiry})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token_oauth2:str, credential_exception):
    try:
        payload = jwt.decode(token_oauth2, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username = username)
    except JWTError:
        raise credential_exception


