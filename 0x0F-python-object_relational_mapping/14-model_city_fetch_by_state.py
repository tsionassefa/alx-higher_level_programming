#!/usr/bin/python3
"""
print all City objects
from the db.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db_uri)
    Session = sessionmaker(bind=eng)

    ses = Session()

    query = session.query(City, State).join(State)

    for _i, _j in query.all():
        print("{}: ({:d}) {}".format(_j.name, _i.id, _i.name))

    ses.commit()
    ses.close()
