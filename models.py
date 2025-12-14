from typing import Optional
from pydantic import BaseModel

#Creating a base model using pydantic
class Product(BaseModel):
    id: Optional[int] = None #Defining that the ID does not need to be provided when creating an item.
    name: str
    price: float