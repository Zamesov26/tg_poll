from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class SubjectSection(Base):
    __tablename__ = 'subject_sections'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)

    subject = relationship('Subject', back_populates='sections')
    terms = relationship('Term', back_populates='subject_section')

    def __str__(self):
        return "<Section (id={}, name={}, subject_name={})>".format(self.id, self.name, self.subject.name)

    def __repr__(self):
        return self.__str__()