from pydantic import BaseModel, Field
from typing import List
class Blog(BaseModel):
    title: str
    body: str


class BlogBase(Blog):
    
    class Config():
        orm_mode = True

class User(BaseModel):
    username: str
    email:str
    password:str


class ShowUsers(BaseModel):
    username: str
    email: str
    blogs_table: List[BlogBase]

    class Config():
        orm_mode = True


class ShowBLog(Blog):
    creator: ShowUsers
    
    class Config():
        orm_mode = True 


class Login(BaseModel):
    username: str
    password:str

    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_types: str

    class Config():
        orm_mode = True 


class TokenData(BaseModel):
    username: str
    
    class Config():
        orm_mode = True 