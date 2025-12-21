#!/usr/bin/env python3

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).where(State.name == sys.argv[4]).first()
    if state:
        print(state.id)
    else:
        print("Not Found")
