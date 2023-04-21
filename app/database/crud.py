from fastapi import HTTPException
from datetime import datetime
from .schemas import *
from sqlalchemy.orm import Session
from . import models

# ------GENERAL CRUD OPERATIONS START HERE------
def add_x(x, db: Session):
    db.add(x)
    db.commit()
    db.refresh(x)
    return x

# ------CRUD OPERATIONS FOR BLOCKS START HERE------
def read_all_blocks(db: Session):
    return db.query(models.Block).all()

def read_block_by_id(db: Session, id: int):
    block = db.query(models.Block).get(id)
    if block is None:
        raise HTTPException(status_code=404, detail='block not found')
    return block

def add_block(block_in: BlockBase, db: Session):
    block = models.Block(**block_in.dict())
    return add_x(block, db)

def delete_block_by_id(id: int, db: Session):
    block = db.query(models.Block).get(id)
    if block is None:
        raise HTTPException(status_code=404, detail='block not found')
    db.delete(block)
    db.commit()
    return {'message': 'block deleted'}

# ------CRUD OPERATIONS FOR PROBES START HERE------
def add_probe(probe_in: ProbeBase, db: Session):
    probe = models.Probe(**probe_in.dict())
    block = db.query(models.Block).get(probe_in.block_id)
    if block is None:
        raise HTTPException(status_code=404, detail='block not found')
    return add_x(probe, db)

def read_all_probes_in_block(id:int, db: Session):
    return db.query(models.Probe).filter(models.Probe.block_id == id).all()

def read_all_probes(db: Session):
    return db.query(models.Probe).all()

def read_probe_by_id(id:int, db: Session, data_limit:int = 10):
    probe: ProbeWithData = db.query(models.Probe).get(id)
    if probe is None:
        raise HTTPException(status_code=404, detail='probe not found')
    probe.data = probe.data[0:data_limit]        
    return probe

def read_probe_data_between_dates(id:int, db: Session, start: str, end:str):
    start_time:datetime = datetime.fromisoformat(start)
    end_time:datetime = datetime.fromisoformat(end)

    probe: ProbeWithData = db.query(models.Probe).get(id)
    if probe is None:
        raise HTTPException(status_code=404, detail='probe not found')
    filtered_data = [x for x in probe.data if start_time <= x.timestamp <= end_time]
    probe.data = filtered_data
    return probe

def delete_probe_by_id(id: int, db: Session):
    probe = db.query(models.Probe).get(id)
    if probe is None:
        raise HTTPException(status_code=404, detail='probe not found')
    db.delete(probe)
    db.commit()
    return {'message': 'probe deleted'}

# ------CRUD OPERATIONS FOR MEASUREMENT DATA START HERE------
# currently only takes utcnow() timestamp, cant manually change data.
def add_measurements(data_in:DataTypeBase, db: Session):
    data_in.timestamp = datetime.utcnow()
    data = models.Data(**data_in.dict())
    probe = db.query(models.Probe).get(data_in.probe_id)
    if probe is None:
        raise HTTPException(status_code=404, detail='probe not found')
    return add_x(data, db)

# need pagination?
def read_all_measurements(db: Session):
    return db.query(models.Data).all()

def read_measurements_by_probe_id(db: Session, id: int):
    return db.query(models.Data).filter(models.Data.probe_id == id).all()