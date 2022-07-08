from fastapi import Form
from pydantic import BaseModel

class UserForm(BaseModel):
    firstname:str
    lastname: str 
    details: str
    
    @classmethod
    def as_form(cls,firstname:str=Form(...),lastname:str=Form(...),details:str=Form(...)):
        return cls(firstname=firstname,lastname=lastname,details=details)
    