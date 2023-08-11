from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base
from unit_of_work import UnitOfWork

engine = create_engine('sqlite:///datebase//base.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

unit_of_work = UnitOfWork(session)
unit_of_work.create_term('intersection')
# unit_of_work.commit()

all_subject = unit_of_work.subject.get_all()
all_section = unit_of_work.section.get_all()
all_term = unit_of_work.term.get_all()
print(all_subject)
print(all_section)
print(all_term)

session.close()
