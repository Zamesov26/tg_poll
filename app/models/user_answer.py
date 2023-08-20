from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, Boolean, String, TIMESTAMP
from sqlalchemy.orm import relationship

from app.models import Base


class UserAnswer(Base):
    __tablename__ = 'user_answers'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    answer_text = Column(String)
    answer_date = Column(TIMESTAMP, default=datetime.utcnow)
    is_correct = Column(Boolean)

    user = relationship("User", back_populates="answers")
    question = relationship("Question", back_populates="user_answers")
