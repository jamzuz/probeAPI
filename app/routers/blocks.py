
from fastapi import APIRouter, Depends
from ..database.crud import read_all_blocks, add_block
from ..database.schemas import BlockBase
from ..database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/blocks')

@router.get('', response_model=list[BlockBase])
def read_blocks(db: Session = Depends(get_db)):
    return read_all_blocks(db)

@router.post('', response_model=BlockBase)
def create_block(block: BlockBase, db: Session = Depends(get_db)):
    return add_block(block, db)

# @router.get('', response_model=list[BandAllListItem])
# def read_bands(name: str = '', db: Session = Depends(get_db)):
#     if name != '':
#         return read_band_by_name(db, name)
#     return read_all_bands(db)


# @router.post('', response_model=BandDb)
# def create_band(band_in: BandBase, db: Session = Depends(get_db)):
#     return save_band(band_in, db)


# @router.get('/{id}', response_model=BandDb)
# def read_band_id(id: int, db: Session = Depends(get_db)):
#     return read_band_by_id(db, id)


# @router.post('/{id}/releases', response_model=ReleaseDb)
# def add_release_for_band(id: int, release_in: ReleaseIn, db: Session = Depends(get_db)):
#     return save_release(id, release_in, db)