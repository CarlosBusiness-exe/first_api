from fastapi import FastAPI
from fastapi import HTTPException #To threat exceptions
from fastapi import status #Pass the status code to be used on the threat

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
async def get_product(id: int): #Type hints because need be converted
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


#Starting using only python command
if __name__ == "__main__":
    import uvicorn

    #Choosing specific configs parameters
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)