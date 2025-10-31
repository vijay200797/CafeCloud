import sys
import os
sys.path.insert(1, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))

from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from app import schemas, database
from sqlalchemy.orm import Session
from app.repository import orders

router = APIRouter(
    prefix="/Order",
    tags=['Orders']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.Order])
def all(db: Session = Depends(get_db)):
    return orders.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Orders, db: Session = Depends(get_db)):
    return orders.create(request, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Order)
def update(id:int, db: Session = Depends(get_db)):
    return orders.update(id, db)
