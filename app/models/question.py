from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'))

    subject = relationship("Subject", back_populates="questions")

    def __repr__(self):
        return f"<Question(id={self.id}, text='{self.text}')>"