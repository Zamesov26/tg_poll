from app.repositories.section import SectionRepository
from app.repositories.subject import SubjectRepository
from app.repositories.term import TermRepository


class UnitOfWork:
    def __init__(self, session):
        self.session = session
        self.subject = SubjectRepository(session)
        self.section = SectionRepository(session)
        self.term = TermRepository(session)

    def create_term(self, term_name, subject_name=None, section_name=None):
        subject = self.subject.get_or_create(subject_name)
        section = self.section.get_or_create(section_name, subject)
        return self.term.get_or_create(term_name, section)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
