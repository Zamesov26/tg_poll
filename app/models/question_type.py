from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.models import Base


class QuestionType(Base):
    __tablename__ = 'question_types'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)

    questions = relationship("Question", back_populates="question_type")

    def __repr__(self):
        return f"<QuestionType(id={self.id}, name='{self.name}')>"
