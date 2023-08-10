from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    sections = relationship('SubjectSection', back_populates='subject')

    def __str__(self):
        return "<class Subject(id={}, name={})>".format(self.id, self.name)

    def __repr__(self):
        return self.__str__()


class SubjectSection(Base):
    __tablename__ = 'subject_sections'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)

    subject = relationship('Subject', back_populates='sections')
    terms = relationship('Term', back_populates='subject_section')


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
