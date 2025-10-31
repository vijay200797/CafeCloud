from sqlalchemy.orm import Session
from app import models, schemas, rabbit_mq
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
    rabbit_mq.publish_order_created(new_order)
    return new_order


def update(id:int, db:Session):
    order = db.query(models.Orders).filter(models.Orders.id == id).first()
    print(order)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with id {id} not found")
    # order.update({schemas.Orders.id : order.id, schemas.Orders.customer_id : order.customer_id, schemas.Orders.status : "C"}, synchronize_session=False)
    # order.update({schemas.Orders.customer_id : order.customer_id, schemas.Orders.status : "C"}, synchronize_session=False)
    order.status = "C"
    db.commit()
    return order