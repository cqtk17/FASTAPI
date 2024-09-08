
from  pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname:str
    database_port : str
    database_password : str
    database_name : str
    database_username : str
    secret_key : str
    algorithm : str
    access_token_expire_minutes : int

    class config:
        env_file = ".env"


settings = Settings()




# những dòng trên dùng để làm gì?
# Đây là cách để chúng ta đọc các biến môi trường từ file .env, sau đó sử dụng chúng trong ứng dụng của mình.
# Đầu tiên, chúng ta tạo một class Settings kế thừa từ BaseSettings của Pydantic.
# Trong class này, chúng ta khai báo các biến môi trường mà chúng ta muốn đọc từ file .env.
# Cuối cùng, chúng ta tạo một instance của class Settings và
# sử dụng các biến môi trường đó trong ứng dụng của mình.
# Cấu hình class Settings với env_file = ".env" để đọc các biến môi trường từ file .env.

# có phải trong bất kì Api nào thì cũng phải tạo venv hay không?
# không, tạo venv chỉ là 1 cách để chúng ta tạo môi trường ảo để cài đặt các thư viện cần thiết cho ứng dụng của mình.
# Nếu bạn không muốn sử dụng venv, bạn cũng có thể cài đặt các thư viện cần thiết trực tiếp trên máy tính của mình.
# Tuy nhiên, việc sử dụng venv sẽ giúp chúng ta tránh được việc xung đột giữa các phiên bản thư viện khác nhau trong ứng dụng của mình.
# Nói chung, việc sử dụng venv là một cách tốt để quản lý các thư viện cần thiết cho ứng dụng của mình.



# Sự quan trọng của file config.py trong ứng dụng FastAPI
# Trong ứng dụng FastAPI, file config.py chứa các biến môi trường cần thiết cho ứng dụng của bạn.
# Các biến môi trường này thường được đọc từ file .env để giữ cho ứng dụng của bạn linh hoạt và dễ dàng cấu hình.
# File config.py giúp chúng ta quản lý các biến môi trường một cách dễ dàng và tránh được việc truy cập trực tiếp vào các biến môi trường trong ứng dụng của mình.
# Điều này giúp chúng ta dễ dàng cấu hình ứng dụng của mình mà không cần phải thay đổi mã nguồn của ứng dụng.
# Ngoài ra, file config.py còn giúp chúng ta quản lý các biến môi trường một cách chuyên nghiệp và dễ dàng mở rộng ứng dụng của mình trong tương lai.


# làm sao biết các biến môi trường được lưu ở đâu để lấy ?
# Để biết các biến môi trường được lưu ở đâu, bạn cần xem file config.py trong ứng dụng của mình.
# Trong file này, bạn sẽ thấy các biến môi trường được khai báo và sử dụng trong ứng dụng của bạn.
# Để lấy các biến môi trường này, bạn cần đọc từ file .env hoặc từ các biến môi trường mà bạn đã cấu hình trước đó.

