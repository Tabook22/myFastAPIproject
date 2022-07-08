from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app=FastAPI()

#define the Item class
class Item(BaseModel):
    name:str
    quantity:float
    price:float
    description:Optional[str]=None #Optional means the description is dosen't should to be there byt if it is there it should be a string




#----------------------------------------
#here we are using a dictionary
inventory={
    1:{
        'name':'Product1',
        'quantity':123,
        'price':321,
        'description':'In The Name of Allah'
    }
}

#----------------------------------------
#here we are using path parameters in the url
@app.get('/getitem/{item_id}')
def getInventory(item_id:int=Path(None,description='Please Add Item Number, and it should be Integer')):
    return inventory[item_id]

#example:'http://127.0.0.1:8000/getitem/1'

#----------------------------------------
#here am using query parameters
@app.get("/get-by-prodcut")
# here am maiking name is optional , using the optional library is recommended by FastAPI, we could use the following "name:str=None" and it will work
# here the asterix "*" means let this function accept unlimited positional arguments, and the ',' means the resut alfter this will be treated as key word arguments
def get_item(*,name:Optional[str]=None,test:int): # Notice Optional means the "name" it may be used or not, but in general should't be there but if it is there it should be a string
    for item_id in inventory:
        if inventory[item_id]['name']==name:
            return inventory[item_id]
    return {'Data':'Not Found'}

#example: http://127.0.0.1:8000/get-by-prodcut?name=Product1&test=2'

#----------------------------------------
#here we combined position arguments with query parameters
@app.get("/get-by-prodcut/{item_id}")
# here am maiking name is optional , using the optional library is recommended by FastAPI, we could use the following "name:str=None" and it will work
# here the asterix "*" means let this function accept unlimited positional arguments, and the ',' means the resut alfter this will be treated as key word arguments
def get_item(*,item_id,name:Optional[str]=None,test:int):
    for item_id in inventory:
        if inventory[item_id]['name']==name:
            return inventory[item_id]
    return {'Data':'Not Found'}

#example:'http://127.0.0.1:8000/get-by-prodcut/1?name=Product1&test=2'



#----------------------------------------
# Using the Reqeust Body, here we are creating a new item in the database
@app.post("/create-item")
def create_item(item:Item):
    pass
