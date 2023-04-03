# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    email: str
    name: str
    telephone: str
    password: str


class UserInputSchema(BaseModel):
    email: str
    name: str
    telephone: str
    password: str


class LoginInputSchema(BaseModel):
    email: str
    password: str


class UserOutputSchema(BaseModel):
    id: int
    email: str
    telephone: str
    name: str

    class Config:
        orm_mode = True


class LoginSuccessSchema(BaseModel):
    user: UserOutputSchema
    access_token: str

    class Config:
        orm_mode = True
