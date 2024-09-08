from fastapi import APIRouter,FastAPI
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import status,Depends
from fastapi.responses import Response
from fastapi.exceptions import HTTPException
from ..import database,schemas,model,utils,oauth2

router=APIRouter(tags=['auth'])

@router.post("/login")
def get_Login(user_credentials:OAuth2PasswordRequestForm = Depends(),db:Session=Depends(database.get_db)):
    user = db.query(model.User).filter(model.User.email==user_credentials.username).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentials")
    
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="invalid credentials")
    
    #crete token
    # return token
    token= oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token":token,"token type":"bearer"}


