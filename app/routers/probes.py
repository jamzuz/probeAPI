
from fastapi import APIRouter, Depends
from ..database.crud import read_all_probes_in_block, add_probe, read_probe_by_id, read_all_probes, delete_probe_by_id, read_probe_data_between_dates
from ..database.schemas import Probe, ProbeBase, ProbeWithData
from ..database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/probes')

# get all probes
@router.get('', response_model=list[Probe])
def read_probes(db: Session = Depends(get_db)):
        """
        Query all probes
        """
        return read_all_probes(db)
# get probe by id
@router.get('/{id}', response_model=ProbeWithData)
def read_a_probe_by_id(id: int, datalimit: int = 10, db: Session = Depends(get_db)):
        """
        Query a probe with id, default measurement data size is limited to 10.
        """
        return read_probe_by_id(id, db, datalimit)
# get probe data between dates
@router.get('/{id}/{start}/{end}', response_model=ProbeWithData)
def read_a_probe_between_dates(id: int, start:str, end:str, db: Session = Depends(get_db)):
        """
        # To search probe data between dates use following format:

        # - **id**: ID of the probe as a number
        # - **start**: start date as an ISO formatted string
        # - **end**: end date as an ISO formatted string
        """
        return read_probe_data_between_dates(id, db, start, end)
# get probes in a block via id
@router.get('/blocks/{id}', response_model=list[Probe]|Probe)
def read_probes_in_a_block(id: int,db: Session = Depends(get_db)):
        """
        Query a block with id, reads all probes in that block.
        """
        return read_all_probes_in_block(id, db)
# create a probe
@router.post('', response_model=ProbeBase)
def create_probe(probe: ProbeBase, db: Session = Depends(get_db)):
        """
        # Create a probe, use following format:
        # - **name**: name of the probe as a string.
        # - **functional**: is the probe functional, true/false.
        # - **block_id**: id of the block the probe is in as a number.
        """
        return add_probe(probe, db)
# delete probe via id
@router.delete('/{id}')
def delete_probe(id: int, db: Session = Depends(get_db)):
        """
        # Delete a probe with probe_id, WARNING DELETES ALL MEASUREMENT DATA FROM PROBE. 
        """
        return delete_probe_by_id(id, db)