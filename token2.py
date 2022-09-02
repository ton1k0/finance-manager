from datetime import datetime, timedelta
from jose import JWTError ,jwt
import schemas, secret

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=secret.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, secret.SECRET_KEY, algorithm=secret.ALGORITHM)
    return encoded_jwt

def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, secret.SECRET_KEY, algorithms=[secret.ALGORITHM])
        name: str = payload.get('sub')
        if name is None:
            raise credentials_exception
        return schemas.TokenData(name=name)
    except JWTError:
        raise credentials_exception