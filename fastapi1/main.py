from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app=FastAPI()


@app.get("/")
def index():
    return {"fastapi":"hello world"}

@app.get('/items/{item}')
async def get_all(item:str):
    return{"item":item}

@app.get("/items/{item_id}")
def read_items(item:int,q: Union[str,None]=None):
    return {"items":item,"q":q}

class Item(BaseModel):
    name:str
    price:int
    is_offer:Union[bool,None]

@app.put("/items/{item_id}")
async def update_item(item:Item, item_id:int):
    return {"item":item.name,"id":item_id, "price":item.price}




@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}



class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get('/items/model_name/{model_name}')
async def showModel(model_name:ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.lenet.value :
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"} 

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"} ]

@app.get('/items/')
async def read_item(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip + limit]

@app.get('/users/{user_id}/items/{item_id}')
async def read_user_items(user_id:int,item_id:str, q:str|None, short:bool=False):
    result={"id":user_id,"item":item_id}

    if q:
        result.update({"q":q})
    if not short:
        result.update({"description":"this is amazing item that has long"})
    return result
class ItemPost(BaseModel):
      name:str
      description:str | None
      price:float
      tax:float | None
@app.post('/item/')
async def post_item(item:ItemPost):
    return item
thislist=['banana','tomato','cacao']
a=thislist.index('tomato')
print(a)