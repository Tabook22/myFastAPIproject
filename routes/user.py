from fastapi import APIRouter
from config.db import conn
from models.index import user 
#from schemas.index import User
from pydantic import BaseModel


appuser=APIRouter()

class User(BaseModel):
    name:str 
    email:str 
    password:str


@appuser.get("/")
async def read_data():
    return conn.execute(user.select()).fetchall()

@appuser.get("/{id}")
async def read_data(id:int):
    return conn.execute(user.select().where(user.c.id== id)).fetchall() # notice:where(users.c.id==id) means where users. column id is equal to id

@appuser.post("/")
#here we define the user as User from the schema
async def write_data(usr:User):
    conn.execute(user.insert().values(
        name=usr.name,
        email=usr.email,
        password=usr.password
        ))
    return conn.execute(user.select()).fetchall()
@appuser.put("/{id}")
async def update_data(id:int, usr:User):
    conn.execute(user.update().values(
        name=usr.name,
        email=usr.email,
        password=usr.password
    ).where(user.c.id==id))
    return conn.execute(user.select()).fetchall()

@appuser.delete("/{id}")
async def delete_data(id:int):
    conn.execute(user.delete().where(user.c.id==id))
    return conn.execute(user.select()).fetchall()