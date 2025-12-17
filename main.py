from fastapi import FastAPI
from fastapi import HTTPException #To threat exceptions
from fastapi import status #Pass the status code to be used on the threat

from fastapi.responses import JSONResponse #Used to return a response in the delete method
from fastapi import Response
from fastapi import Path #To use path parameters
from fastapi import Query #To use query parameters
from fastapi import Header #To use header parameters
from typing import List, Optional

from models import Product #Using the model that was created

app = FastAPI()

#Creating ditcs of dicts
products = {
    1:{
        "name":"Rice",
        "price":10.5
    },
    2:{
        "name":"Bean",
        "price":9.5
    },
    3:{
        "name":"Meat",
        "price":20.0
    }
}

#GET METHOD - Read
#Get all products
@app.get("/products")
async def get_products():
    return products

#Get one product
@app.get("/products/{id}") #In keys because is a variable(python)
#Type hints, and using path parameter to describe the function and limit the values
#gt- greater than, lt- lower than.
#Descriptions appear on the /docs
#The path parameter is used to set rules and a lot of things related with the path. Ctrl+click in Path to see all the things
async def get_product(id: int = Path(default=None, title="Product ID", description="Have to be between 0 - 100", gt=0, lt=100)):
    try: #Try to find and return the product
        return products[id] #Returning the product
    #This will change, the server will not broke, only return the 404 error, and continue working
    except KeyError: #If get a Keyerror(didn't exist the key sended)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found.") #What will be returned(error not found with description)


#POST METHOD - Create
#Create a new item
#Have to be sent the parameters on the body of the request
@app.post("/products" , status_code=status.HTTP_201_CREATED) #Using status code only to set the right status when create a element
async def post_product(product: Product): #Python hints of the model type
    next_id: int = len(products) + 1 #Python hints to convert, get the size of products(last id) + 1
    products[next_id] = product #Set this new product on the position(on  the key-> next_id:dict)
    return product

    """Manually validation
    if product.id not in products:
        products[product.id] = product
        return product
    else: #if it is already on the datas, raise a erro of conflict
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Already have a product with this id: {product.id}")"""
    
#PUT METHOD - Update
@app.put("/products/{product_id}") #Passing the id of the product that will be deleted on the url
async def put_products(product_id: int, product: Product):
    if product_id in products: #Verifying if exist a product with this id
        products[product_id] = product #If it exist, will update it
        return product
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product Id not found.") #Rainsing a error mensage with was used a invalid id

#DELETE METHOD - Delete
@app.delete("/products/{product_id}") #Pass the id on the url
async def delete_product(product_id: int):
    if product_id in products: #If exist a element with this id
        del products[product_id] #Delete it
        #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, detail="The product was deleted") #Returning a status code of JSON to a deleted content
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product id not found") #Raise a error if is not found

@app.get("/calculator")
#Need to pass the arguments on the querys(after "?")
#If I try to execute this by passing only the variables without specifying their type(python hints), the code will simply concatenate the "texts"
#The GET url -> http://localhost:8000/calculator?a=10&b=2&c=21
#Exemple of using a optional variable
#I can pass rules to query, in the same way of paths
async def calculator(a: int = Query(default=None, gt=0, lt=999), b: int = Query(default=None, gt=10, lt=999), x_header: str = Header(default=None), c: int = Query(default=None, gt=0, lt=999), d: Optional[int] = None):
    result = a + b + c
    optional_result = result

    #To set header partameters, it has to be passed on the header area of the request
    print(f"X_HEADER: {x_header}")

    if d:
        optional_result = optional_result + d
    return(f"Normal result: {result},Result with optional: {optional_result}")

"""
    Path Parameter: Used to specify WHO you want (which ID, which specific item).

    Query Parameter: Used to specify HOW you want it (filtered, sorted, limited).
"""

#Starting using only python command
if __name__ == "__main__":
    import uvicorn

    #Choosing specific configs parameters
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)