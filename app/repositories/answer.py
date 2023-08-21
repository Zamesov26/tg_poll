from sqlalchemy.orm import Session
from app.models import Answer, Question
from typing import List, Optional


class AnswerRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all_answer(self):
        return self.session.query(Answer).all()

    def get_answer_by_id(self, answer_id: int) -> Optional[Answer]:
        return self.session \
            .query(Answer) \
            .filter(Answer.id == answer_id) \
            .first()

    def get_answers_by_question_id(self, question_id: int) -> List[Answer]:
        return self.session \
            .query(Answer) \
            .filter(Answer.question_id == question_id) \
            .all()

    def get_answer_by_question_id_and_text(self, question_id: int, text: str):
        return self.session \
            .query(Answer) \
            .filter(Answer.question_id == question_id, Answer.text == text) \
            .first()

    def create_answer(self, question_id: int, text: str,
                      is_true: bool = False) -> Answer:
        new_answer = Answer(question_id=question_id,
                            text=text,
                            is_true=is_true)
        self.session.add(new_answer)
        return new_answer

    def delete_answer(self, answer: Answer):
        self.session.delete(answer)

    def get_or_create(self, answer_text: str, question: Question):
        for answer in question.answers():
            if answer == answer_text:
                return answer
        return self.create_answer()
