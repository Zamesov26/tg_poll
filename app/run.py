from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base
from unit_of_work import UnitOfWork

engine = create_engine('sqlite:///datebase//base.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

unit_of_work = UnitOfWork(session)

#

session.close()
