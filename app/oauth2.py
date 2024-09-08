
from datetime import datetime,timedelta
# pip install python-jose [cryptography]
from jose import jwt,JWTError
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from . import schemas,database,model
from sqlalchemy.orm import Session
from .config import Settings,settings
# Secret key
# algorithim
# expiration time
# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60

SECRET_KEY =settings.secret_key
ALGORITHM =settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES =settings.access_token_expire_minutes

OAuth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

def verify_access_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exception
        token_data=schemas.tokenData(id=str(id))
    except JWTError as e:
        print(e)
        raise credentials_exception
    return token_data

def get_current_user(token : str = Depends(OAuth2_scheme),db:Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="could not vaiidate credentials",headers={"WWW-Authenticate":"bearer"})
    
    token=verify_access_token(token,credentials_exception)
    user= db.query(model.User).filter(model.User.id==token.id).first()
    return token
