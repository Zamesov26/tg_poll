from sqlalchemy import Column, Integer, ForeignKey, JSON, String
from sqlalchemy.orm import relationship

from app.models import Base


class UserState(Base):
    __tablename__ = 'user_states'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    state = Column(String, default='start')
    data = Column(JSON, default="{}")

    user = relationship("User", back_populates="states")
