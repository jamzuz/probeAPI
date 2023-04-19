from pydantic import BaseModel

# base type for all blocks, containes the block name
class BlockBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

# extends base type adding 'id'' to it, this autoincrements and cannot be changed as it is the primary key for it
class Block(BlockBase):
    id: int
#  data that the probe collects

class Data(BaseModel):
    temp: float
    time: str

# probe base
class ProbeBase(BaseModel):
    name: str
    functional: bool = True
    block_id: int
    
    class Config:
        orm_mode = True

# extends base type adding 'id'' to it, this autoincrements and cannot be changed as it is the primary key for it
# also adds the block_id field telling in what block the probe is
class Probe(ProbeBase):
    id: int
    # data: list[Data]
    
# adds probe field to the data to identify what probe collected it(possibly moot)
class DataBaseModel(Data):
    probe: Probe



