from sqlalchemy.orm import Session
from app import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Orders).all()
    return blogs


def create(request: schemas.Orders, db: Session):
    new_order = models.Orders(
    id = None,    
    customer_id=request.customer_id,
    status="N" #,
    # order_items  = []
    # order_items=[models.OrderItems(id = None, name = item.name, qty = item.qty) for item in request.order_items]
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order


