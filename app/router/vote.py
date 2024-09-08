from fastapi import APIRouter,FastAPI

from fastapi import status,Depends
from fastapi.responses import Response
from fastapi.exceptions import HTTPException

from .. import model,schemas,utils,database,oauth2
from ..database import get_db
from sqlalchemy.orm import Session
router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)



@router.post("/",status_code=status.HTTP_201_CREATED)
def create_vote(vote:schemas.vote,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    post = db.query(model.Post).filter(model.Post.id == vote.post_id).first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {vote.post_id} not found")
    vote_query = db.query(model.Vote).filter(model.Vote.post_id == vote.post_id,model.Vote.user_id == current_user.id)
    vote_exists = vote_query.first()
    if dir == True:
        if vote_exists:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="You have already voted")
        new_vote = model.Vote(post_id=vote_exists.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"Vote created"}
    if dir == False:
        if vote_exists is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="You have not voted")
        db.delete(vote_exists)
        db.commit()
        return {"message":"Vote removed"}
        