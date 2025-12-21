#!/usr/bin/env python3

import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')

    Session = sessionmaker(bind=engine)
    session = Session()
    
    state = session.query(State).first()
    if state:
        print(f'{state.id}: {state.name}')
    else:
        print("Nothing")
