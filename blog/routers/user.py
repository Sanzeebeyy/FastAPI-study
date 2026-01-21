from fastapi import APIRouter, Depends,status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..hashing import Hash

router = APIRouter(
    prefix="/user",
    tags=["Users"]
    )


@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(request.password) # bcrypt is a function created in Hash Class in hashing.py
    new_user = models.User(username = request.username, email = request.email, password = hashed_password )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/' ,response_model=List[schemas.ShowUsers])
def show_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get('/{id}',status_code=200 ,response_model=schemas.ShowUsers)
def get_user_by_id(id:int , db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {f"Blog with {id} is not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The User with id: {id} is not found")
    return user