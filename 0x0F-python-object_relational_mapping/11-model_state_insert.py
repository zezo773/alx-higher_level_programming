#!/usr/bin/env python3

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()

    st = State(name="Louisiana")
    session.add(st)
    session.commit()

    val = session.query(State).where(State.name == "Louisiana").first()
    if val:
        print(val.id)
