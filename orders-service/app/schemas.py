from typing import List, Optional
from pydantic import BaseModel


class Orders(BaseModel):
    cutomer_id: str
    status: str