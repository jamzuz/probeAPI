from fastapi import HTTPException
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

# ------CRUD OPERATIONS FOR PROBES START HERE------
def add_probe(probe_in: ProbeBase, db: Session):
    probe = models.Probe(**probe_in.dict())
    return add_x(probe, db)

def read_all_probes_in_block(id:int, db: Session):
    return db.query(models.Probe).filter(models.Probe.block_id == id)

def read_all_probes(db: Session):
    return db.query(models.Probe).all()

def read_probe_by_id(id:int, db: Session):
    probe = db.query(models.Probe).get(id)
    if probe is None:
        raise HTTPException(status_code=404, detail='probe not found')
    return probe

# def read_band_by_id(db: Session, id: int):
#     band = db.query(models.Band).filter(models.Band.id == id).first()
#     if band is None:
#         raise HTTPException(status_code=404, detail='band not found')
#     return band


# def read_band_by_name(db: Session, name: str):
#     band = db.query(models.Band).filter(models.Band.name == name).all()
#     if band is None:
#         raise HTTPException(status_code=404, detail='band not found')
#     return band


# def save_band(band_in: BandBase, db: Session):
#     band = models.Band(**band_in.dict())
#     db.add(band)
#     db.commit()
#     db.refresh(band)
#     return band


# def save_release(id: int, release_in: ReleaseBase, db: Session):
#     rel = models.Release(**release_in.dict(), band_id=id)
#     db.add(rel)
#     db.commit()
#     db.refresh(rel)
#     return rel