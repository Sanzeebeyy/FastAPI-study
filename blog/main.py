from fastapi import FastAPI, Depends
from . import schemas, models
from .database import engine, LocalSession
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()



@app.post('/blog')
def create(blog:schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title = blog.title, body = blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}')
def get_blog_by_id(id:int , db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog