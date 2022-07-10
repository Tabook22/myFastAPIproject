from fastapi import FastAPI 
from routes.index import appuser

app=FastAPI()

app.include_router(appuser)