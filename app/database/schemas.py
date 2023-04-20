from pydantic import BaseModel

# There are blocks, probes and data
# every block has 0-n probes
# and every probe has 0-n amount of data

#  data that the probe collects
class DataTypeBase(BaseModel):
    measurement: float
    timestamp: str
    probe_id: int

    class Config:
        orm_mode = True
        # fields = {'probe_id': {'exclude' : True}}

class DataType(DataTypeBase):
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

# no reason to show block_id in this class because it only comes up when looking up blocks via id
class ProbeInBlock(Probe):
    class Config:
        fields = {'block_id': {'exclude' : True}}


class BlockBase(BaseModel):
    name: str

    class Config:
        orm_mode = True

# extends base type adding 'id'' to it, this autoincrements and cannot be changed as it is the primary key for it
# also contains a list of probes belonging to this block
class Block(BlockBase):
    id: int
    probes: list[ProbeInBlock] 

