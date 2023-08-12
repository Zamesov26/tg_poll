from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)

    sections = relationship('SubjectSection', back_populates='subject')
    questions = relationship('Question', back_populates='subject')

    def __str__(self):
        return "<class Subject(id={}, name={})>".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()
