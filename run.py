from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from unit_of_work import UnitOfWork

engine = create_engine('sqlite:///base.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

unit_of_work = UnitOfWork(session)
# unit_of_work.subject.create('python')
print(unit_of_work.subject.get_all())

session.close()
