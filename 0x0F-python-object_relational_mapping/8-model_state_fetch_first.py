#!/usr/bin/python3
"""
prints the first State object
from the database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db_uri)
    Session = sessionmaker(bind=eng)

    ses = Session()
    instance = ses.query(State).order_by(State.id).first()

    if instance is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(instance.id, instance.name))
