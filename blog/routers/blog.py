from fastapi import APIRouter, Depends,status, HTTPException
from .. import schemas, models, oauth2
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
    )

@router.get('/' , response_model=List[schemas.ShowBLog])
def get_all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(blog:schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title = blog.title, body = blog.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/{id}' , status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "deleted"


@router.put('/{id}' , status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog:schemas.Blog, id:int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).update(blog.dict(exclude_unset=True))
    db.commit()
    return "Updated"


@router.get('/{id}',status_code=200, response_model=schemas.ShowBLog)
def get_blog_by_id(id:int  , db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The Blog with id: {id} is not found")
    return blog