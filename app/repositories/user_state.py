from sqlalchemy.orm import Session

from app.models import UserState


class UserStateRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_user_id(self, user_id: int):
        return self.session \
            .query(UserState) \
            .filter(UserState.user_id == user_id) \
            .first()

    def create(self, user):
        user_state = UserState(user=user)
        self.session.add(user_state)

    def update(self, user_id, new_state, data):
        state = self.get_by_user_id(user_id)
        state.state = new_state
        state.data = data
