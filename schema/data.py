from pydantic import BaseModel

class Data(BaseModel):
    name: str
    accountNumber: int
    type: str

    class config:
        orm_mode = True