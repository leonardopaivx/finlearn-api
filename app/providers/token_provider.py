from jose import jwt
from datetime import datetime, timedelta
from app.config.settings import setting

# CONFIG
SECRET_KEY = setting.SECRET_KEY
ALGORITHM = "HS256"
EXPIRES_IN_MIN = 10080


def create_access_token(data: dict):
    dataset = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    dataset.update({"exp": expiration})

    jwt_token = jwt.encode(dataset, key=SECRET_KEY, algorithm=ALGORITHM)

    return jwt_token


def verify_acess_token(token: str):
    data_load = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return data_load.get("sub")
