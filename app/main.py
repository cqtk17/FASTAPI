
from fastapi import FastAPI






from . import model
from .database import engine
from sqlalchemy.orm import Session
# chạy môi trường ảo bằng lệnh uvicorn app.main:app --reload mỗi sự thay đổi sẽ được cập nhật
from .router import post, user,auth,vote


model.Base.metadata.create_all(bind=engine) # tạo bảng trong database
app= FastAPI() # tạo 1 ứng dụng FastAPI


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
   








@app.get('/')
def root():

    return {'message':'Chao mung ban den voi FastAPI !!!'}












# so sánh giữa pydantic và sqlalchemy models
# Pydantic models are used to validate the request body data and to serialize the response data.
# SQLAlchemy models are used to interact with the database.
# Pydantic models are used to validate the request body data and to serialize the response data.
# SQLAlchemy models are used to interact with the database.
# read more at https://stackoverflow.com/questions/71570607/sqlalchemy-models-vs-pydantic-models
# read sqlalchemy at https://docs.sqlalchemy.org/en/14/orm/tutorial.html

# venv\Scripts\activate -- kích hoạt môi trường ảo

# tìm hiểu về JWT token
# https://viblo.asia/p/tim-hieu-ve-json-web-token-jwt-7rVRqp73v4bP

# tìm hiểu về cookie và session
#https://viblo.asia/p/tim-hieu-ve-cookies-bXP4W5YKL7G 