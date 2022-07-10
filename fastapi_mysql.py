#source:https://www.youtube.com/watch?v=4Zy90rd0bkU
from fastapi import FastAPI 
from routes.user import appuser

app=FastAPI()

app.include_router(appuser)