from sqlalchemy.orm import Session

from app.models import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_users(self):
        return self.session \
            .query(User) \
            .all()

    def get_user_by_name(self, name: str):
        return self.session \
            .query(User) \
            .filter(User.name == name) \
            .first()

    def get_user_by_tg_id(self, tg_id: int):
        return self.session \
            .query(User) \
            .filter(User.tg_id == tg_id) \
            .first()

    def create_user(self, name: str, tg_name: str = None, tg_id: int = None):
        user = User(name=name, tg_name=tg_name, tg_id=tg_id)
        self.session.add(user)
        return user
