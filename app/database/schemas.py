from pydantic import BaseModel

# base type for all blocks, containes the block name
class BlockBase(BaseModel):
    name: str

    class Config:
        orm_mode = True