#!/usr/bin/env python3

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name = session.query(State).filter(State.id == 2).first()
    if state_name:
        state_name.name = "New Mexico"
        session.commit()
