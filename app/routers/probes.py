
from fastapi import APIRouter, Depends
from ..database.crud import read_all_probes_in_block, add_probe, read_probe_by_id, read_all_probes, delete_probe_by_id, edit_probe_block_by_id, put_probe_in_error_state, read_all_errors, read_probes_by_state, restore_probe
from ..database.schemas import Probe, ProbeWithData, Error, ProbeInBlock
from ..database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/probes', tags=['Probes'])

# get all probes
@router.get('', response_model=list[Probe])
def read_probes(db: Session = Depends(get_db)):
        """
        # Query all probes
        """
        return read_all_probes(db)
# get probe by id
@router.get('/{id}', response_model=ProbeWithData)
def read_a_probe_by_id(id: int, datalimit: int = 10, db: Session = Depends(get_db), start:str = None, end:str = None):
        """
        # Query a probe with id, default measurement data size is limited to 10.

        # To search probe data between dates use following format:

        - **id**: ID of the probe as a number
        - **datalimit**: number of temperature data results to include in the response(default is 10)
        - **start**: start date as an ISO formatted string(YYYY-MM-DDTHH:mm:SS)
        - **end**: end date as an ISO formatted string
        """
        return read_probe_by_id(id, db, datalimit, start, end)

# get probes in a block via id
@router.get('/blocks/{id}', response_model=list[ProbeInBlock]|ProbeInBlock)
def read_probes_in_a_block(id: int,db: Session = Depends(get_db)):
        """
        # Query a block with id, reads all probes in that block.
        # Returns most recent temperature reading with the probe.
        """
        return read_all_probes_in_block(id, db)
# create a probe
@router.post('', response_model=Probe)
def create_probe(name:str, functional:bool, block_id:int, db: Session = Depends(get_db)):
        """
        # Create a probe, use following format:
        # - **name**: name of the probe as a string.
        # - **functional**: is the probe functional, true/false.
        # - **block_id**: id of the block the probe is in.
        """
        return add_probe(name, functional, block_id, db)
# edit probe
@router.put('/{id}')
def edit_probe_block(id:int, block_id: int, db: Session = Depends(get_db)):
        """
        # Edit a probes block_id:
        # - **id**: id of the probe.
        # - **block_id**: id of the new block probe is in.
        """
        return edit_probe_block_by_id(id, db, block_id)
# edit probe state
@router.put('/error/{id}', response_model=Error )
def set_probe_in_error_state(id:int, db: Session = Depends(get_db)):
        """
        # Puts probe in error state with current time as timestamp:
        # - **id**: id of the probe.
        """
        return put_probe_in_error_state(id, db)
# restore probe state
@router.put('/functional/{id}', response_model=Probe )
def restore_probe_state(id:int, db: Session = Depends(get_db)):
        """
        # Puts probe in functional state
        # - **id**: id of the probe.
        """
        return restore_probe(id, db)
# get probe by state
@router.get('/functional/', response_model=list[Probe])
def get_probe_by_state(functional:bool, db: Session = Depends(get_db)):
        """
        # Find all probes in state
        # - **functional**: Is the probe functional, true/false.
        """
        return read_probes_by_state(functional,db)
#get errors
@router.get('/errors/', response_model=list[Error] )
def get_all_errors(db: Session = Depends(get_db)):
        """
        # Get all errors, returns timestamps, probe_id and id of the error
        """
        return read_all_errors(db)
# delete probe via id
@router.delete('/{id}')
def delete_probe(id: int, db: Session = Depends(get_db)):
        """
        # Delete a probe with probe_id, WARNING DELETES ALL MEASUREMENT DATA FROM PROBE. 
        """
        return delete_probe_by_id(id, db)