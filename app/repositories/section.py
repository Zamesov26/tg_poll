from sqlalchemy.orm import Session

from app.models import SubjectSection


class SectionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session \
            .query(SubjectSection) \
            .all()

    def get_by_id(self, section_id):
        return self.session \
            .query(SubjectSection) \
            .filter_by(id=section_id) \
            .first()

    def get_all_by_name(self, section_name):
        return self.session \
            .query(SubjectSection) \
            .filter_by(name=section_name) \
            .all()

    def get_or_create(self, section_name, subject):
        for section in self.get_all_by_name(section_name):
            if section.subject is subject:
                return section
        section = SubjectSection(name=section_name, subject=subject)
        self.session.add(section)

        return section
