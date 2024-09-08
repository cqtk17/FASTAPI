
from fastapi import FastAPI

from fastapi import status,Depends
from fastapi.responses import Response
from fastapi.exceptions import HTTPException
import time
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .. import model,schemas,utils,database,oauth2
from ..database import get_db
from sqlalchemy.orm import Session

from fastapi import APIRouter
router=APIRouter(
    prefix="/user",
    tags=['User']
)



@router.post("/",status_code= status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.Usercreate,db:Session=Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    hashed_password=utils.hash(user.password)
    user.password=hashed_password
    new_user=model.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id:int,db:Session=Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    print(current_user.email)
    user = db.query(model.User).filter(model.User.id == id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {id} not found")
    
    return user