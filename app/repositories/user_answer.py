from sqlalchemy.orm import Session

from app.models import UserAnswer


class UserAnswerRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_answer(self):
        return self.session.query(UserAnswer).all()

    def get_all_answer_by_user_id(self, user_id: int):
        return self.session.query(UserAnswer).filter(
            UserAnswer.user_id == user_id).all()

    def create_user_answer(self, user_id: int, question_id: int,
                           answer_text: str, is_correct: bool):
        user_answer = UserAnswer(user_id=user_id,
                                 question_id=question_id,
                                 answer_text=answer_text,
                                 is_correct=is_correct)
        self.session.add(user_answer)
        return user_answer
