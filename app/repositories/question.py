from sqlalchemy.orm import Session
from app.models import Question


class QuestionRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, text: str, question_type='text'):
        question = Question(text=text, question_type=question_type)
        self.session.add(question)
        return question

    def get_all_by_text(self, question_text: int):
        return self.session \
            .query(Question) \
            .filter(Question.text == question_text) \
            .all()

    def get_all(self):
        return self.session.query(Question).all()

    def get_questions_by_subject(self, subject_id: int):
        return self.session \
            .query(Question) \
            .filter(Question.subject_id == subject_id) \
            .all()
