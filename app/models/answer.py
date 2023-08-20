from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base

class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    text = Column(String, nullable=False)
    is_true = Column(Boolean, nullable=False, default=False)

    question = relationship("Question", back_populates="answers")


    def __repr__(self):
        return f"<Answer(id={self.id}, text='{self.text}', is_true={self.is_true}, type_id={self.type_id})>"
