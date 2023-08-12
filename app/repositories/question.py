from sqlalchemy.orm import Session
from app.models import Question


class QuestionRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, text: str, subject):
        question = Question(text=text, subject=subject)
        self.session.add(question)
        self.session.commit()
        self.session.refresh(question)
        return question

    def get_by_id(self, question_id: int):
        return self.session \
            .query(Question) \
            .filter(Question.id == question_id) \
            .first()

    def get_all_by_text(self, question_text: int):
        return self.session \
            .query(Question) \
            .filter(Question.text == question_text) \
            .all()

    def get_all(self):
        return self.session.query(Question).all()

    def update_text(self, question_id: int, new_text: str):
        question = self.get_by_id(question_id)
        if question:
            question.text = new_text
            self.session.commit()
            self.session.refresh(question)
        return question

    def delete(self, question_id: int):
        question = self.get_by_id(question_id)
        if question:
            self.session.delete(question)
            self.session.commit()

    def get_questions_by_subject(self, subject_id: int):
        return self.session \
            .query(Question) \
            .filter(Question.subject_id == subject_id) \
            .all()

    def get_or_create(self, text, subject):
        for question in self.get_all_by_text(text):
            if question.subject is subject:
                return question
        question = Question(text=text, subject=subject)
        self.session.add(question)

        return question

