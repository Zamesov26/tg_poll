from typing import Tuple, Optional

from app.repositories import (
    SectionRepository, SubjectRepository, TermRepository, QuestionRepository,
    UserAnswerRepository, UserRepository, AnswerRepository,
    UserStateRepository,
)


class UnitOfWork:
    def __init__(self, session):
        self.session = session

        self.subject = SubjectRepository(session)
        self.section = SectionRepository(session)
        self.term = TermRepository(session)
        self.question = QuestionRepository(session)
        self.answer = AnswerRepository(session)
        self.user = UserRepository(session)
        self.user_answer = UserAnswerRepository(session)
        self.user_state = UserStateRepository(session)

    def create_term(self, term_name, subject_name=None, section_name=None):
        subject = self.subject.get_or_create(subject_name)
        section = self.section.get_or_create(section_name, subject)
        return self.term.get_or_create(term_name, section)

    def create_question(self, text, list_answers: list[Tuple[str, bool]],
                        subject_name: Optional[str] = None,
                        question_type='text'):
        subject = self.subject.get_or_create(subject_name)
        question = self.question.get_question_by_text_end_subject(text,
                                                                  subject.id)
        if not question:
            question = self.question.create(text=text,
                                            question_type=question_type)
            subject.questions.append(question)

        for text_answer, is_true in list_answers:
            answer = self.answer.create(text=text_answer, is_true=is_true)
            question.answers.append(answer)

        return question

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
