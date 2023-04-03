# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
from pydantic import BaseModel


class IdOut(BaseModel):
    id: int

    class Config:
        orm_mode = True
