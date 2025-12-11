from typing import Optional
from pydantic import BaseModel

#Creating a base model using pydantic
class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price: float