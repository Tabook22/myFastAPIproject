import uvicorn 
from fastapi import FastAPI, Request, Form, Depends 
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
from schemas import UserForm

#start our fastapi applicaiton
app=FastAPI()

templates=Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def hello_world():
    return {"message":"In The Name of Allah"}


@app.get('/items', response_class=HTMLResponse)
def read_item(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post('/items',response_class=HTMLResponse)
#def post_details(request:Request, firstname:str=Form(...), lastname:str=Form(...),details:str=Form(...)):
async def post_details(request:Request, form_data:UserForm=Depends(UserForm.as_form)):
    #print(f'First Name: {firstname}')
    #print(f'Last Name: {lastname}')
    #print(f'Details: {details}')
    #return templates.TemplateResponse("index.html",{"request":request,"firstname":firstname, "lastname":lastname})
    print(form_data)
    return templates.TemplateResponse("index.html",{"request":request})


if __name__=='__main__':
    uvicorn.run(app)
