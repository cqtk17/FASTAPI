from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@
# {settings.database_hostname}:{settings.database_port}/{settings.database_name}'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


engine= create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base= declarative_base()

def get_db(): # lấy database nếu chưa có sẽ tạo cái mới
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True: # kết nối với database
#     try: 
#         conn=psycopg2.connect(host='localhost', database='fastapi', user='postgres',password='25102004', cursor_factory=RealDictCursor)
#         cur=conn.cursor()
#         print("Connected to the database successfully!!!")
#         break
#     except Exception as error:
#         print("Could connect to the database!!!")
#         print("Error:",error)
#         time.sleep(2)