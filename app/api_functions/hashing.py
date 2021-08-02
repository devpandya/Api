from passlib.context import CryptContext 

pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")


class Hash():
    def bcrypt(string:str):
        return pwd_cxt.hash(string)

    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)
