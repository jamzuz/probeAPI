from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class Block(Base):
    __tablename__ = 'blocks'

    # Define the primary key column for the Block table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    # Define the one-to-many relationship between Probe and Block
    # Set up cascade delete for Probe table when a Block is deleted to delete all associated probes
    probes = relationship('Probe', backref='probes', cascade='all, delete-orphan')

class Probe(Base):
    __tablename__ = 'probes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    functional = Column(Boolean, nullable=False, default=True)
    block_id = Column(Integer, ForeignKey('blocks.id'), nullable=False)
    # when deleting a probe all data is also deleted
    data = relationship('Data', backref='data', cascade='all, delete-orphan')

class Data(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    probe_id = Column(Integer, ForeignKey('probes.id'), nullable=False)
    timestamp = Column(DateTime)
    measurement = Column(Float)