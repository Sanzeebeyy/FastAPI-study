from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str

class ShowBLog(Blog):
    class Config():
        orm_mode = True

class User(BaseModel):
    username: str
    email:str
    password:str
