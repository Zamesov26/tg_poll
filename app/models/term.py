from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Term(Base):
    __tablename__ = 'terms'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subject_section_id = Column(Integer, ForeignKey('subject_sections.id'),
                                nullable=False)
    description = Column(String)
    translate = Column(String)
    image = Column(String)

    subject_section = relationship('SubjectSection', back_populates='terms')

    def __str__(self):
        return "<Term (id={}, name={}, section={})>".format(self.id, self.name, self.subject_section.name)

    def __repr__(self):
        return self.__str__()
