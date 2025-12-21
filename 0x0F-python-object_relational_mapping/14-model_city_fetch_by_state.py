#!/usr/bin/env python3

from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State.name, City.id, City.name).filter(State.id == City.state_id)
    for value in data:
        print(f'{value[0]}: ({value[1]}) {value[2]}')
