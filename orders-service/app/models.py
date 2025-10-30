from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base
from sqlalchemy.orm import relationship, Mapped
from  typing import List
import datetime


class Orders(Base):
    __tablename__ = 'orders'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(String)
    status = Column(String, default = "N")
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    # items = relationship("OrderItems", back_populates="order", cascade="all, delete-orphan")
    order_items: Mapped[List["OrderItems"]] = relationship("app.models.OrderItems", backref="order_items")


class OrderItems(Base):
    __tablename__ = 'order_items'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    name = Column(String)
    qty = Column(Integer)
    
    # order = relationship("Orders", back_populates="items")
    # order: Mapped["Orders"] = relationship("app.models.Orders", back_populates="order_items")

    
