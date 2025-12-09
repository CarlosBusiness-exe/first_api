from fastapi import FastAPI

#Instace the class
app = FastAPI()

#The bar is the source page(base)
#Decorator é tipo uma plaquinha: "Sempre que alguém chegar no site procurando pelo endereço principal (/) usando o método GET (navegador), mande essa pessoa falar com a função read_root."
@app.get("/")
async def source(): #Function that defines what will happens when do a get on the source page
        return {"msg": "FastApi is running!"} #Returning a dictionary that will be formated on JSON only to see

#I can execute the api only with "python first_fastapi.py"
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("first_fastapi:app", host="127.0.0.1", port=8000, log_level="info", reload=True) #OBS: seu eu usar o ip "0.0.0.0", qualquer pessoa da rede pode acessar a api, usando o ip