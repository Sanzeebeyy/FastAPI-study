from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/blog")
def index(limit:int = 99, published:bool = True, sort:str|None = None):
    if published:
        return ({"data": f"{limit} blogs from DataBase are published"})
    else:
        return{"Nalla":"Hai Kya?"}

@app.get("/blog/unpublished")
def unpublished():
    return {"data":"all unpublished blogs"}

@app.get("/blog/{id}")
def show(id:int):
    return {"data":id}


@app.get("/blog/{id}/comment")
def comment(id, limit:int = 10):
    # fetch comments with id == id
    return {"data":[1,2,3,4,5, f"{limit} ota matra comment"]}



class Blog(BaseModel):
    title: str
    body: str
    published: bool|None = None


@app.post('/blog')
def create_blog(blog:Blog):
    return{"Data":f"Blog is created with title: {blog.title}"}

