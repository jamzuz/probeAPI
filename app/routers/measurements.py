
from fastapi import APIRouter, Depends
from ..database.crud import add_measurements, read_all_measurements, delete_measurement_by_id
from ..database.schemas import DataType, DataTypeBase
from ..database.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix='/measurements', tags=['Measurements'])

@router.get('', response_model=list[DataType])
def read_measurements(db: Session = Depends(get_db)):
    """
    # read all measurements
    """
    return read_all_measurements(db)

@router.post('', response_model=DataTypeBase)
def add_measurement(measurement:float, probe_id:int, timestamp:str = None, db: Session = Depends(get_db)):
    """
    # add a measurement manually, use following format:
    # - **measurement**: temperature in celcius(eg. 25.4) *note that the temperature is rounded to the nearest decimal.
    # - **timestamp**: when was the measurement taken, in ISO formatted string(YYYY-MM-DDTHH:mm:SS). if no timestamp given uses current time
    # - **probe_id**: id of the probe that generated the result.
    """
    return add_measurements(measurement, probe_id, timestamp, db)

@router.delete('/{id}')
def delete_measurement(id: int, db:Session = Depends(get_db)):
    """
    # Delete measurement with id
    """
    return delete_measurement_by_id(id, db)
