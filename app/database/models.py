from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .database import Base

class Block(Base):
    __tablename__ = 'blocks'

    # Define the primary key column for the Block table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Probe(Base):
    __tablename__ = 'probes'

    # Define the primary key column for the Probe table
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    functional = Column(Boolean, nullable=False, default=True)
    # Define the foreign key column for the Block table
    block_id = Column(Integer, ForeignKey('blocks.id'), nullable=False)
    # Define the one-to-many relationship between Probe and Block
    block = relationship('Block', backref='probes')
