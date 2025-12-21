from typing import Optional
from pydantic import BaseModel, validator #Validator is used to customize de validations of pydantic

#Creating a base model using pydantic
class Product(BaseModel):
    id: Optional[int] = None #Defining that the ID does not need to be provided when creating an item.
    name: str
    price: float

    #The valitador shold be on the class
    @validator("name") #Creating a custom validetation to nname
    def validate_name(cls, value: str): #Cls is "class", value pick what is passed in the validator
        words = value.split(" ") #Cut the value(name) in the spaces, and create a list
        if len(words) < 2:
            raise ValueError("The name shold have at list 2 words")
        
        if value.islower():
            raise ValueError("The name shold be capitalized")
        
        return value
    
    @validator("price")
    def validate_price(cls, value: float):
        if value < 0:
            raise ValueError("The price shold be greater then 0")
        
        return value

products = [
    Product(id = 1, name = "Rice Weller", price = 10.5),
    Product(id = 2, name = "Bean Jorge", price = 9.35)
]