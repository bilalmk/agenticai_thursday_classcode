from pydantic import BaseModel

class UserData(BaseModel):
    name:str
    age:int

user1 = UserData(name="Ratan lal", age=33)

# print(user1)