#!/usr/bin/python3
"""
it is city class to work with mysqlalchemy orm
"""

from model_state import Base,State
from sqlalchemy import Column, Integer, String, Foreignkey


class City(Base):
    """
    creating class and attributes
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_Key=True)
    name = Column(String(128), nullable=False)
    state_id= Column(Integer, ForeignKey('states.id'), nullable=False)
