from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Orders).all()
    return blogs


def create(request: schemas.Orders, db: Session):
    print(request)
    # ab =[models.OrderItems(name = item.name, qty = item.qty) for item in request.items]
    # # for item in request.items:
    # #     print(item.name + str(item.qty) )
    # print(ab)
    # new_order = models.Orders(customer_id=request.customer_id, status="N")
    new_order = models.Orders(
    id = None,    
    customer_id=request.customer_id,
    status="N",
    # order_items  = []
    order_items=[models.OrderItems(id = None, name = item.name, qty = item.qty) for item in request.order_items]
    )

    # for item in request.items:
    #     # print(item.name + str(item.qty) )
    #     new_order.order_items.append(models.OrderItems(id = None, name = item.name, qty = item.qty))

    db.add(new_order)
    print("1" + new_order)
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