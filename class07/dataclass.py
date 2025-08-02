from dataclasses import dataclass
from pydantic import BaseModel


# @dataclass
# class User:
#     name: str
#     id: int


class User(BaseModel):
    name: str
    id: int


def get_name(u: User):
    u.id="adfsdf"
    print(u.name)
    print(u.id)


user = User(name="Bilal", id=1)

get_name(user)
