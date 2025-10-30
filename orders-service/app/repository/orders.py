from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Orders).all()
    return blogs


def create(request: schemas.Orders, db: Session):
    new_order = models.Orders(customer_id=request.cutomer_id, status=request.status)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


# def destroy(id: int, db: Session):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)

#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} not found")

#     blog.delete(synchronize_session=False)
#     db.commit()
#     return 'done'


# def update(id: int, request: schemas.Blog, db: Session):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)

#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} not found")

#     blog.update(request)
#     db.commit()
#     return 'updated'


# def show(id: int, db: Session):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with the id {id} is not available")
#     return blog