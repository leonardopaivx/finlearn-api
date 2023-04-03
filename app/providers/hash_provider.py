from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


def generate_hash(text):
    return pwd_context.hash(text)


def verify_hash(text, hashed_text):
    return pwd_context.verify(text, hashed_text)
