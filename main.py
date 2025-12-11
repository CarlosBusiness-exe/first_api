from fastapi import FastAPI
from fastapi import HTTPException #To threat exceptions
from fastapi import status #Pass the status code to be used on the threat

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

#GET METHOD
#Get all products
@app.get("/products")
async def get_products():
    return products

#Get one product
@app.get("/products/{id}") #In keys because is a variable
async def get_product(id: int): #Type hints because need be converted
    try: #Try to find and return the product
        return products[id] #Returning the product
    #This will change, the server will not broke, only return the 404 error, and continue working
    except KeyError: #If get a Keyerror(didn't exist the key sended)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found.") #What will be returned(error not found with description)


#Starting using only python command
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)