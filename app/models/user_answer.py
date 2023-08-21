from datetime import datetime

from sqlalchemy import (Column, Integer, ForeignKey, Boolean, String,
                        TIMESTAMP, Table)
from sqlalchemy.orm import relationship

from app.models import Base

user_answer_to_option = Table(
    'user_answer_to_option',
    Base.metadata,
    Column('user_answer_id', Integer, ForeignKey('user_answers.id')),
    Column('answer_id', Integer, ForeignKey('answers.id'))
)

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
    selected_answers = relationship("Answer", secondary=user_answer_to_option)
