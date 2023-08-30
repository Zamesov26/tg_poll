from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tg_name = Column(String)
    tg_id = Column(Integer, nullable=False, default=False)

    answers = relationship('UserAnswer', back_populates="user")
    states = relationship("UserState", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', tg_name={self.tg_name}, tg_id={self.tg_id})>"
