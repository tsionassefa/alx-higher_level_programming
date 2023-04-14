#!/usr/bin/python3
"""
define city to work with mysql alchemy orm
"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """
    creating class and attributes
    """
     __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

