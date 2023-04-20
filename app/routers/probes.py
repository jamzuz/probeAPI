
from fastapi import APIRouter, Depends
from ..database.crud import read_all_probes_in_block, add_probe, read_probe_by_id, read_all_probes, delete_probe_by_id
from ..database.schemas import Probe, ProbeBase, Block
from ..database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/probes')

# can return a list of probe or single probe depending if id is given.
@router.get('', response_model=list[Probe]|Probe)
def read_probes(id: int = None,db: Session = Depends(get_db)):
    if id is not None:
        return read_probe_by_id(id, db)
    else:
        return read_all_probes(db)
    
@router.get('/blocks/{id}', response_model=list[Probe]|Probe)
def read_probes_in_a_block(id: int,db: Session = Depends(get_db)):
        return read_all_probes_in_block(id, db)
        
@router.post('', response_model=ProbeBase)
def create_probe(probe: ProbeBase, db: Session = Depends(get_db)):
    return add_probe(probe, db)

@router.delete('/{id}')
def delete_probe(id: int, db: Session = Depends(get_db)):
    return delete_probe_by_id(id, db)