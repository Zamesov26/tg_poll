import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base
from app.repositories import (
    SubjectRepository, SectionRepository, TermRepository, QuestionRepository,
    QuestionTypeRepository, AnswerRepository, UserRepository
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
def question_type_repository(test_db_session):
    return QuestionTypeRepository(session=test_db_session)


@pytest.fixture(scope="function")
def some_question_type(question_type_repository):
    question_type = question_type_repository.get_or_create('some_question_type')
    return question_type


@pytest.fixture(scope="function")
def question_repository(test_db_session):
    return QuestionRepository(session=test_db_session)


@pytest.fixture(scope="function")
def some_question(some_subject, question_repository, some_question_type):
    question = question_repository.get_or_create('some_question', some_subject)
    some_question_type.questions.append(question)
    return question


@pytest.fixture(scope="function")
def answer_repository(test_db_session):
    return AnswerRepository(session=test_db_session)


@pytest.fixture(scope="function")
def user_repository(test_db_session):
    return UserRepository(session=test_db_session)