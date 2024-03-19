#!/usr/bin/python3
"""
This script lists all State objects
from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

if __name__ == "__main__":
    """
    Connect to the database and extract required data
    """
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
             argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print('{}: {}'.format(instance.id, instance.name))
