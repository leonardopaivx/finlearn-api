from pydantic import BaseModel


class IdOut(BaseModel):
    id: int

    class Config:
        orm_mode = True
