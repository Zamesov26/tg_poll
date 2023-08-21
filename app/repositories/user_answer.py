from typing import Optional

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
                           is_correct: bool = None,
                           answer_text: Optional[str] = None,
                           answer_lst: Optional[list] = None):
        user_answer_data = {
            'user_id': user_id,
            'question_id': question_id,
            'is_correct': is_correct
        }

        if answer_lst:
            user_answer = UserAnswer(**user_answer_data,
                                     selected_answers=answer_lst)
        else:
            user_answer = UserAnswer(**user_answer_data,
                                     answer_text=answer_text)

        self.session.add(user_answer)
        return user_answer
