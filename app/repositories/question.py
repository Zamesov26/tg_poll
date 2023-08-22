from sqlalchemy.orm import Session
from app.models import Question


class QuestionRepository:
    def __init__(self, session: Session):
        self.session = session

<<<<<<< HEAD
    def create(self, text: str, question_type='text'):
        question = Question(text=text, question_type=question_type)
        self.session.add(question)
=======
    def create(self, text: str, subject):
        question = Question(text=text, subject=subject)
>>>>>>> 9b3ecbcba4e59beab0b922a44925d6d5923b2f22
        return question

    def get_all_by_text(self, question_text: int):
        return self.session \
            .query(Question) \
            .filter(Question.text == question_text) \
            .all()

    def get_all(self):
        return self.session.query(Question).all()

<<<<<<< HEAD
=======
    def update_text(self, question_id: int, new_text: str):
        question = self.get_by_id(question_id)
        if question:
            question.text = new_text
        return question

    def delete(self, question_id: int):
        question = self.get_by_id(question_id)
        if question:
            self.session.delete(question)

>>>>>>> 9b3ecbcba4e59beab0b922a44925d6d5923b2f22
    def get_questions_by_subject(self, subject_id: int):
        return self.session \
            .query(Question) \
            .filter(Question.subject_id == subject_id) \
            .all()
<<<<<<< HEAD
=======

    def get_or_create(self, text, subject):
        for question in self.get_all_by_text(text):
            if question.subject is subject:
                return question
        question = Question(text=text, subject=subject)
        self.session.add(question)

        return question
>>>>>>> 9b3ecbcba4e59beab0b922a44925d6d5923b2f22
