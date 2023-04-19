
from fastapi import APIRouter, Depends
from ..database.crud import read_all_probes_in_block, add_probe, read_probe_by_id, read_all_probes
from ..database.schemas import Probe, ProbeBase, Block
from ..database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/probes')

# can return a list of probe or single block depending if id is given.
@router.get('', response_model=list[Probe]|Probe)
def read_probes_in_block(id: int = None,db: Session = Depends(get_db)):
    if id is not None:
        return read_probe_by_id(id, db)
    else:
        return read_all_probes(db)
    
@router.post('', response_model=ProbeBase)
def create_probe(probe: ProbeBase, db: Session = Depends(get_db)):
    return add_probe(probe, db)

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