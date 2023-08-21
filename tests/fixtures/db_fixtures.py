import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base
from app.repositories import (
    SubjectRepository, SectionRepository, TermRepository, QuestionRepository,
    AnswerRepository, UserRepository, UserAnswerRepository
)


@pytest.fixture(scope="function")
def test_db_session():
    engine = create_engine("sqlite:///:memory:")
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    yield session

    session.close()


@pytest.fixture(scope="function")
def subject_repository(test_db_session):
    return SubjectRepository(session=test_db_session)


@pytest.fixture(scope="function")
def some_subject(subject_repository):
    subject = subject_repository.get_or_create("some_subject")
    return subject


@pytest.fixture(scope="function")
def section_repository(test_db_session):
    return SectionRepository(session=test_db_session)


@pytest.fixture(scope="function")
def term_repository(test_db_session):
    return TermRepository(session=test_db_session)


@pytest.fixture(scope="function")
def question_repository(test_db_session):
    return QuestionRepository(session=test_db_session)


@pytest.fixture(scope="function")
def some_question(some_subject, question_repository, some_question_type):
    question = question_repository.get_or_create('some_question', some_subject)
    some_question_type.questions.append(question)
    return question

@pytest.fixture(scope="function")
def some_question_text(some_subject, question_repository, some_question_type):
    question = question_repository.create('some_question', some_subject)
    some_question_type.questions.append(question)
    return question

@pytest.fixture(scope="function")
def some_question_with_answers(some_question, answer_repository):
    answers = [('вариант1', False), ('вариант2', True), ('вариант3', False),
               ('вариант4', False), ('вариант5', False), ('вариант6', False)]

    for text, is_true in answers:
        answer_repository.create_answer(text=text, is_true=is_true,
                                        question_id=some_question.id)

    return some_question


@pytest.fixture(scope="function")
def answer_repository(test_db_session):
    return AnswerRepository(session=test_db_session)


@pytest.fixture(scope="function")
def user_repository(test_db_session):
    return UserRepository(session=test_db_session)


@pytest.fixture(scope="function")
def some_user(user_repository):
    user = user_repository.create_user(name='some_user', tg_id=1234)
    return user


@pytest.fixture(scope="function")
def user_answer_repository(test_db_session):
    return UserAnswerRepository(session=test_db_session)
