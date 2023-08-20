from sqlalchemy.orm import Session
from app.models import QuestionType
from typing import Optional


class QuestionTypeRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_answer_type_by_id(self, answer_type_id: int) -> Optional[QuestionType]:
        return self.session \
            .query(QuestionType) \
            .filter(QuestionType.id == answer_type_id) \
            .first()

    def get_answer_type_by_name(self, name: str) -> Optional[QuestionType]:
        return self.session \
            .query(QuestionType) \
            .filter(QuestionType.name == name) \
            .first()

    def get_all_answer_types(self):
        return self.session.query(QuestionType).all()

    def create_answer_type(self, name: str, description: str) -> QuestionType:
        new_answer_type = QuestionType(name=name, description=description)
        self.session.add(new_answer_type)
        return new_answer_type

    def delete_answer_type(self, answer_type: QuestionType):
        self.session.delete(answer_type)

    def get_or_create(self, name):
        answer_type = self.get_answer_type_by_name(name)
        if not answer_type:
            answer_type = QuestionType(name=name)
            self.session.add(answer_type)
        return answer_type
