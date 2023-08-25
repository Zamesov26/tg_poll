from sqlalchemy.orm import Session
from app.models import Answer, Question
from typing import List, Optional


class AnswerRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_answer(self):
        return self.session.query(Answer).all()


    def get_answer_by_question_id_and_text(self, question_id: int, text: str):
        return self.session \
            .query(Answer) \
            .filter(Answer.question_id == question_id, Answer.text == text) \
            .first()

    def create_answer(self, text: str, is_true: bool = False) -> Answer:
        new_answer = Answer(text=text,
                            is_true=is_true)
        self.session.add(new_answer)
        return new_answer

    def delete_answer(self, answer: Answer):
        self.session.delete(answer)
