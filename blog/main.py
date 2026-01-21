from fastapi import FastAPI
# from fastapi import FastAPI, Depends, status, Response, HTTPException
# from . import schemas, models
from . import models
from .database import engine
# from .database import engine, LocalSession, get_db
# from sqlalchemy.orm import Session
# from typing import List
# from .hashing import Hash
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)

app.include_router(user.router)

app.include_router(authentication.router)







# def get_db():
#     db = LocalSession()
#     try:
#         yield db
#     finally:
#         db.close()



# @app.post('/blog',tags=["blog"] , status_code=status.HTTP_201_CREATED)
# def create(blog:schemas.Blog, db:Session = Depends(get_db)):
#     new_blog = models.Blog(title = blog.title, body = blog.body, user_id = 1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog



# @app.delete('/blog/{id}',tags=["blog"] , status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id: int, db: Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     db.commit()
#     return "deleted"


# @app.put('/blog/{id}',tags=["blog"] , status_code=status.HTTP_202_ACCEPTED)
# def update_blog(blog:schemas.Blog, id:int, db: Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id).update(blog.dict(exclude_unset=True))
#     db.commit()
#     return "Updated"






# @app.get('/blog/{id}',status_code=200, tags=["blog"] ,response_model=schemas.ShowBLog)
# def get_blog_by_id(id:int , response:Response , db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Blog with id: {id} is not found")
#     return blog


# @app.post('/user', tags=["user"])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     hashed_password = Hash.bcrypt(request.password) # bcrypt is a function created in Hash Class in hashing.py
#     new_user = models.User(username = request.username, email = request.email, password = hashed_password )
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user', tags=["user"] ,response_model=List[schemas.ShowUsers])
# def show_users(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users

# @app.get('/user/{id}',status_code=200, tags=["user"] ,response_model=schemas.ShowUsers)
# def get_user_by_id(id:int , db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {f"Blog with {id} is not available"}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The User with id: {id} is not found")
#     return user
