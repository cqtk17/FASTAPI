from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import model, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/post",
    tags=['Post']
)

router.get("/",response_model=list[schemas.Post])
def post(db:Session=Depends(get_db),current_user:int =Session(oauth2.get_current_user),limit: int =10,skip:int =0,search:Optional[str]="" ):
     #cur.execute(""" SELECT * FROM "Posts";""")
     #posts=cur.fetchall()
    posts = db.query(model.Post).filter(model.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts

@router.get('/sqlalchemy',response_model=list[schemas.Postout])
def get_posts(db:Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user), limit: int =10,skip:int =0,search:Optional[str]=""):
    # posts= db.query(model.Post).filter((model.Post.owner_id) == int (current_user.id)).all()
    posts = db.query(model.Post, func.count(model.Vote.post_id).label("votes")).join(
        model.Vote, model.Vote.post_id == model.Post.id, isouter=True).group_by(model.Post.id).filter(model.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts



@router.post("/createpost",status_code= status.HTTP_201_CREATED,response_model=schemas.Post)
def creatpost(new_post:schemas.createPost,db:Session=Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    #cur.execute("""Insert into "Posts" (title,content,published) values (%s,%s,%s) returning * ; """,
     #           (new_post.title,new_post.content,new_post.published))
    #post=cur.fetchone()
    #conn.commit()
    #print(**new_post.dict())
    #post = model.Post(new_post.title,new_post.content,new_post.published) - 1 cách lấy new_post
    
    
    post = model.Post(owner_id=current_user.id,**new_post.dict())# tạo 1 post mới, lấy dữ liệu từ new_post
    db.add(post)
    db.commit()
    db.refresh(post)
    return  post



@router.get("/{id}",response_model=schemas.Postout)
def get_post(id:int,db:Session=Depends(get_db),response_model=schemas.Post, current_user: int = Depends(oauth2.get_current_user)):
     #cur.execute("""Select * from "Posts" where id=%s;""",(str(id))) - truy vấn trực tiếp từ database
     #post=cur.fetchone()
    # post_query=db.query(model.Post).filter(model.Post.id==id)
    # post=post_query.first()
    # if(post==None):
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Your post ID: {id} is not found") 
    # if str(post.owner_id) != (current_user.id):
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=" You can't access this post")
    # return post
    post = db.query(model.Post, func.count(model.Vote.post_id).label("votes")).join(
        model.Vote, model.Vote.post_id == model.Post.id, isouter=True).group_by(model.Post.id).filter(model.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")

    return post


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def Delete_post(id:int,db:Session=Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    #cur.execute("""Delete from "Posts" where id=%s returning *; """,(str(id)))
    #post=cur.fetchone()
    post_query=db.query(model.Post).filter(model.Post.id==id)
    post=post_query.first()
    if(post==None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Your post ID: {id} is not found") 
    if str(post.owner_id) != (current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=" You can't access this post")
    #conn.commit()
    db.delete(post)
    db.commit()
    
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,post:schemas.Post,db:Session=Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    #cur.execute("""update "Posts" set title=%s,content=%s where id=%s returning *;""",(post.title,post.content,str(id)))
    #New_post=cur.fetchone()
    post_query= db.query(model.Post).filter(model.Post.id==id)
    post_one=post_query.first()

    if(post_one==None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Your post ID: {id} is not found") 
    if str(post_one.owner_id) != (current_user.id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=" You can't access this post")
    #conn.commit()
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()
    