from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class Block(Base):
    __tablename__ = 'blocks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)


    
# class Band(Base):
#     __tablename__ = 'bands'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     formed = Column(Integer, nullable=tuple)

#     releases = relationship('Release', back_populates='band')


# class Release(Base):
#     __tablename__ = 'releases'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     year_published = Column(Integer, nullable=False)
#     band_id = Column(Integer, ForeignKey('bands.id'))

#     band = relationship('Band', back_populates='releases')