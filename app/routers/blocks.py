
from fastapi import APIRouter, Depends
from ..database.crud import read_all_blocks, add_block, read_block_by_id, delete_block_by_id
from ..database.schemas import BlockBase, Block
from ..database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/blocks')

# can return a list of blocks or single block depending if id is given.
@router.get('', response_model=list[Block]|Block)
def read_blocks(id: int = None,db: Session = Depends(get_db)):
    if id is not None:
        return read_block_by_id(db, id)
    else:
        return read_all_blocks(db)

@router.post('', response_model=BlockBase)
def create_block(block: BlockBase, db: Session = Depends(get_db)):
    return add_block(block, db)

@router.delete('/{id}')
def delete_block(id: int, db: Session = Depends(get_db)):
    return delete_block_by_id(id, db)
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