from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from sqlalchemy.orm import relationship
import datetime


class Orders(Base):
    __tablename__ = 'orders'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(String)
    status = Column(String, default = "N")
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    

