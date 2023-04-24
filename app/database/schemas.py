from pydantic import BaseModel
from datetime import datetime

# There are blocks, probes and data
# every block has 0-n probes(in spec this is 1-n but everything start with creating a block)
# every probe has 0-n amount of data
# and 0-n amount of errors

#  data that the probe collects
class DataTypeBase(BaseModel):
    measurement: float
    timestamp: datetime
    probe_id: int

    class Config:
        orm_mode = True

class DataType(DataTypeBase):
    id: int

class ErrorBase(BaseModel):
    time_of_error: datetime
    probe_id: int

    class Config:
        orm_mode = True

class Error(ErrorBase):
    id: int

class ProbeBase(BaseModel):
    name: str
    functional: bool = True
    block_id: int
    
    class Config:
        orm_mode = True

# extends base type for probe adding 'id'' to it, this autoincrements and cannot be changed as it is the primary key for it
class Probe(ProbeBase):
    id: int

class ProbeWithData(Probe):
    data: list[DataType]

class ProbeWithErrors(Probe):
    errors: list[Error]

class ProbeInBlock(Probe):
    data: list[DataType]

class BlockBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

# extends base type adding 'id'' to it, this autoincrements and cannot be changed as it is the primary key for it
# also contains a list of probes belonging to this block
class Block(BlockBase):
    id: int
    probes: list[ProbeInBlock] 

class Blocks(BlockBase):
    id: int
    probes: list[ProbeBase]
