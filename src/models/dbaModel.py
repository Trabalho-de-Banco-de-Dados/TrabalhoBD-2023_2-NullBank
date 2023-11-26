from pydantic import BaseModel

class DbaModel(BaseModel):
    sql: str
