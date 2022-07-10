import os
import uuid
import uvicorn 
from fastapi import FastAPI, Request, Form, Depends ,File,UploadFile
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse #this allow us to use a link or url to see the files
from fastapi.staticfiles import StaticFiles 
from fastapi.templating import Jinja2Templates
from schemas import UserForm


#start our fastapi applicaiton
app=FastAPI()

#this path for storing files and use it to check if the files exists or not
path="myfastapiproject/files"

templates=Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def hello_world():
    return {"message":"In The Name of Allah"}


@app.get('/items', response_class=HTMLResponse)
def read_item(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post('/items')#,response_class=HTMLResponse)
async def post_details(request:Request, 
                       firstname:str=Form(...), 
                       lastname:str=Form(...),
                       details:str=Form(...),
                       cvfile:UploadFile = File(...)):
#the async method means that there are some response still in the background (will be displyed in the future), and we should wait for it in the client side
#async def post_details(request:Request, form_data:UserForm=Depends(UserForm.as_form)):
    #request_object_content = await cvfile.read()
    #file_location = f"files/{cvfile.filename}"
    cvfile.filename=f"{uuid.uuid4}.jpg"
    contents = await cvfile.read() # <-- Important!
    # example of how you can save the file
    with open(cvfile.filename, "wb") as f:
        f.write(contents)
    #with open('test1.png', "wb") as image:
    #    image.write(cvfile)
    #    image.close()
        
    print(f'First Name: {firstname}')
    #print(cvfile.filename)
    #print(f'Last Name: {lastname}')
    #print(f'Details: {details}')
    #return templates.TemplateResponse("index.html",{"request":request,"firstname":firstname, "lastname":lastname})
    #print(form_data)
    return templates.TemplateResponse("index.html",{"request":request,"filename": cvfile.filename})


if __name__=='__main__':
    uvicorn.run(app)
