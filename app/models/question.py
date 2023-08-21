from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .base import Base

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    question_type = Column(Enum('single_choice', 'multiple_choice', 'text'),
                           default='single_choice')

    subject = relationship("Subject", back_populates="questions")
    answers = relationship("Answer", back_populates="question")
    user_answers = relationship("UserAnswer", back_populates="question")

    def __repr__(self):
        return f"<Question(id={self.id}, text='{self.text}')>"
