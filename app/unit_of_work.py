from app.repositories import (
    SectionRepository, SubjectRepository, TermRepository, QuestionRepository,
    UserAnswerRepository, UserRepository, AnswerRepository,
    QuestionTypeRepository
)


class UnitOfWork:
    def __init__(self, session):
        self.session = session

        self.subject = SubjectRepository(session)
        self.section = SectionRepository(session)
        self.term = TermRepository(session)
        self.question_type = QuestionTypeRepository(session)
        self.question = QuestionRepository(session)
        self.answer = AnswerRepository(session)
        self.user = UserRepository(session)
        self.user_answer = UserAnswerRepository(session)

    def create_term(self, term_name, subject_name=None, section_name=None):
        subject = self.subject.get_or_create(subject_name)
        section = self.section.get_or_create(section_name, subject)
        return self.term.get_or_create(term_name, section)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
