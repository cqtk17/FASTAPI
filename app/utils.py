from passlib.context import CryptContext
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")# tạo 1 đối tượng để mã hóa mật khẩu, sử dụng bcrypt để mã hóa mật khẩu


def hash(password:str):
    return pwd_context.hash(password)

def verify(plain_password,hashed_passwword):
    return pwd_context.verify(plain_password,hashed_passwword) # hàm này sẽ so sánh mật khẩu đã mã hóa với mật khẩu chưa mã hóa, nếu trùng nhau sẽ trả về True, ngược lại trả về False