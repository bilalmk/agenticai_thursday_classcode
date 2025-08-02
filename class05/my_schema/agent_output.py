from pydantic import BaseModel

class MyDataOutput(BaseModel):
    n1:int 
    n2:int
    response:str = "Thanks"
