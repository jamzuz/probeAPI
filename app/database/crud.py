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

def add_block(name:str, db: Session):
    block = models.Block(name = name)
    return add_x(block, db)

def delete_block_by_id(id: int, db: Session):
    block = db.query(models.Block).get(id)
    if block is None:
        raise HTTPException(status_code=404, detail='block not found')
    db.delete(block)
    db.commit()
    return {'message': 'block deleted'}

def read_all_probes_in_block(id:int, db: Session):
    block: Block = db.query(models.Block).get(id)
    if block is None:
        raise HTTPException(status_code=404, detail='block not found')
    probes = block.probes
    # sort in reverse order by timestamp so newest is first, slice giving only first result showing most recent reading.
    for probe in probes:
        probe.data.sort(key=lambda x: x.timestamp ,reverse=True)
        probe.data = probe.data[0:1]
    return probes

# ------CRUD OPERATIONS FOR PROBES START HERE------

def add_probe(name:str, functional:bool, block_id:int, db: Session):
    block = db.query(models.Block).get(block_id)
    if block is None:
        raise HTTPException(status_code=404, detail='block not found')
    probe = models.Probe(name=name, functional=functional, block_id=block_id)
    return add_x(probe, db)

def read_all_probes(db: Session):
    return db.query(models.Probe).all()

def read_probe_by_id(id:int, db: Session, data_limit:int = 10, start: str = None, end:str = None):
    probe: ProbeWithData = db.query(models.Probe).get(id)
    if probe is None:
        raise HTTPException(status_code=404, detail='probe not found')
    if end is not None:
        if start is None:
            raise HTTPException(status_code=400, detail='start date not provided')
    if start is not None:
        if end is None:
            raise HTTPException(status_code=400, detail='end date not provided')
        else:
            try:
                start_time:datetime = datetime.fromisoformat(start)
                end_time:datetime = datetime.fromisoformat(end)
                probe.data = [probe for probe in probe.data if start_time <= probe.timestamp <= end_time]
            except ValueError:
                raise HTTPException(status_code=400, detail='date in wrong format, use (YYYY-MM-DDTHH:mm:SS) ')
                
    probe.data = probe.data[0:data_limit]        
    return probe

def read_probes_by_state(functional:bool, db: Session):
    return db.query(models.Probe).filter(models.Probe.functional == functional).all()
def restore_probe(id:int, db: Session):
    probe: Probe = db.query(models.Probe).get(id)
    if probe is None:
        raise HTTPException(status_code=404, detail='probe not found')
    probe.functional = True
    db.commit()
    db.refresh(probe)
    return probe


def edit_probe_block_by_id(id:int, db: Session, block_id: int):
    probe: Probe = db.query(models.Probe).get(id)
    if probe is None:
        raise HTTPException(status_code=404, detail='probe not found')
    block = db.query(models.Block).get(block_id)
    if block is None:
        raise HTTPException(status_code=404, detail='block not found')
    
    probe.block_id = block_id
    db.commit()
    db.refresh(probe)
    return probe


def delete_probe_by_id(id: int, db: Session):
    probe = db.query(models.Probe).get(id)
    if probe is None:
        raise HTTPException(status_code=404, detail='probe not found')
    db.delete(probe)
    db.commit()
    return {'message': 'probe deleted'}

# ------CRUD OPERATIONS FOR MEASUREMENT DATA START HERE------

def add_measurements(measurement:int, probe_id:int, timestamp:str, db: Session):
    if timestamp is None:
        timestamp = datetime.utcnow()
    else:
        timestamp = datetime.fromisoformat(timestamp)
    data = models.Data(measurement = round(measurement, 1), timestamp = timestamp, probe_id = probe_id)
    probe: Probe = db.query(models.Probe).get(data.probe_id)
    if probe is None:
        raise HTTPException(status_code=404, detail='probe not found')
    if probe.functional is False:
        raise HTTPException(status_code=400, detail='probe is not functional')
    return add_x(data, db)

def read_all_measurements(db: Session):
    return db.query(models.Data).all()

def delete_measurement_by_id(id:int, db: Session):
    measurement = db.query(models.Data).get(id)
    if measurement is None:
        raise HTTPException(status_code=404, detail='measurement not found')
    db.delete(measurement)
    db.commit()
    return {'message': 'measurement deleted'}

# ------CRUD OPERATIONS FOR ERROR DATA START HERE------

def read_all_errors(db: Session):
    return db.query(models.Errors).all()

def put_probe_in_error_state(id: int, db: Session):
    error_time = datetime.utcnow()
    probe: Probe = db.query(models.Probe).get(id)
    if probe is None:
        raise HTTPException(status_code=404, detail='probe not found')
    error = models.Errors(probe_id = id, time_of_error = error_time)
    probe.functional = False
    return add_x(error, db)