from sqlalchemy.orm import Session

from app.models import Subject


class SubjectRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session \
            .query(Subject) \
            .all()

    def get_by_id(self, subject_id):
        return self.session \
            .query(Subject) \
            .filter_by(id=subject_id) \
            .first()

    def get_by_name(self, subject_name):
        return self.session \
            .query(Subject) \
            .filter_by(name=subject_name) \
            .first()

    def get_or_create(self, name):
        subject = self.get_by_name(name)
        if not subject:
            subject = Subject(name=name)
            self.session.add(subject)
            self.session.commit()
        return subject
