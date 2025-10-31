from typing import List, Optional
from pydantic import BaseModel

class OrderItems(BaseModel):
    name: str
    qty : int

class Orders(BaseModel):
    customer_id: str
    order_items: List[OrderItems] = []

class Order(BaseModel):
    id : int
    customer_id: str
    status : str
    