from fastapi import FastAPI

#instintiate fastapi objects
app=FastAPI()

#create your first endpoing
#here we are using the decorate
@app.get('/')
def index():
    return {'key':'value'}