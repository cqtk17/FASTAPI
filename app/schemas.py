
from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class PostBase(BaseModel): # tạo 1 class Post kế thừa BaseModel
     title:str
     content:str
     published: bool = True


class createPost(PostBase): # tạo 1 class createPost kế thừa PostBase, tại sao phải có class này, vì khi client gửi dữ liệu lên server, dữ liệu đó sẽ được lưu vào class này, sau đó sẽ được truyền vào class Post
    pass



class UserOut(BaseModel):
    email:EmailStr
    id:int
    create_at:datetime

    class Config:
        orm_mode=True



class Post(PostBase): # tạo 1 class Post kế thừa PostBase, dể trả về dữ liệu cho client
     id:int
     create_at:datetime
     owner_id:int
     owner : UserOut #
      
     class Config:# cấu hình cho class Post, để không trả về dữ liệu id và create_at cho client nếu không cần thiết
        orm_mode = True


class Postout(BaseModel):
    Post:Post
    vote_count:int
    class Config:
        orm_mode=True

class Usercreate(BaseModel):
    email:EmailStr
    password:str
class User(BaseModel):
    email:EmailStr
    hashed_password:str

    class Config:
        orm_mode=True


class userlogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class tokenData(BaseModel):
    id:Optional[str] = None

class vote(BaseModel):
    post_id:int
    dir: bool