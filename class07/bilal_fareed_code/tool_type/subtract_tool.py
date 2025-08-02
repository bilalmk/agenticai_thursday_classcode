from pydantic import BaseModel


class SubtractSchema(BaseModel):
    n1:int
    n2:int