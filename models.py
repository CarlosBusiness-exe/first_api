from typing import Optional
from pydantic import BaseModel

#Creating a base model using pydantic
class Product(BaseModel):
    id: Optional[int] = None #Set that id is not necessary be provided when will create a item
    name: str
    price: float