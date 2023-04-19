from fastapi import HTTPException
from .schemas import BlockBase
from sqlalchemy.orm import Session

from . import models

def read_all_blocks(db: Session):
    return db.query(models.Block).all()

def add_block(block_in: BlockBase, db: Session):
    block = models.Block(**block_in.dict())
    db.add(block)
    db.commit()
    db.refresh(block)
    return block

# def read_all_bands(db: Session):
#     return db.query(models.Band).all()


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