
from fastapi import APIRouter, Depends
from ..database.crud import read_all_blocks, add_block, read_block_by_id, delete_block_by_id
from ..database.schemas import Block, Blocks
from ..database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/blocks', tags=['Blocks'])

# can return a list of blocks or single block depending if id is given.
@router.get('', response_model=list[Blocks]|Blocks)
def read_blocks(id: int = None,db: Session = Depends(get_db)):
    """
    # Send query without id to query all blocks, or search a single block with id 
    """
    if id is not None:
        return read_block_by_id(db, id)
    else:
        return read_all_blocks(db)

@router.post('', response_model=Block)
def create_block(name:str, db: Session = Depends(get_db)):
    """
    # Create a block with name as a string 
    """
    return add_block(name, db)

@router.delete('/{id}')
def delete_block(id: int, db: Session = Depends(get_db)):
    """
    # Delete a block with block id.
    # WARNING 
    # THIS DELETES ALL DATA ASSOCIATED WITH THE BLOCK INCLUDING PROBES AND PROBE DATA 
    """
    return delete_block_by_id(id, db)