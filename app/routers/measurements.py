
from fastapi import APIRouter, Depends
from ..database.crud import add_measurements, read_all_measurements, read_measurements_by_probe_id
from ..database.schemas import DataType, DataTypeBase
from ..database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/measurements')

# # can return a list of measurements or a single measurement depending if id is given.
@router.get('', response_model=list[DataType]|DataType)
def read_measurements(id: int = None,db: Session = Depends(get_db)):
    if id is not None:
        return read_measurements_by_probe_id(db, id)
    else:
        return read_all_measurements(db)

@router.post('', response_model=DataTypeBase)
def add_measurement(data: DataTypeBase, db: Session = Depends(get_db)):
    return add_measurements(data, db)

# @router.delete('')
# def delete_block(id: int, db: Session = Depends(get_db)):
#     return delete_block_by_id(id, db)
