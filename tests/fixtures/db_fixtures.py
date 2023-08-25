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
def subject_fixture(subject_repository):
    subject = subject_repository.get_or_create("test_subject")
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
def text_question_fixture(question_repository):
    question = question_repository.create('text_question',
                                          question_type='text')
    return question


@pytest.fixture(scope="function")
def single_question_fixture(question_repository, answer_repository):
    question = question_repository.create('single_question',
                                          question_type='single_question')

    answers = [('вариант1', True), ('вариант2', False), ('вариант3', False),
               ('вариант4', False), ('вариант5', False), ('вариант6', False)]

    for text, is_true in answers:
        question.answers.append(
            answer_repository.create_answer(text=text, is_true=is_true)
        )

    return question


@pytest.fixture(scope="function")
def multiple_question_fixture(question_repository, answer_repository):
    question = question_repository.create('multiple_question',
                                          question_type='multiple_choice')

    answers = [('вариант1', True), ('вариант2', True), ('вариант3', False),
               ('вариант4', False), ('вариант5', False), ('вариант6', False)]

    for text, is_true in answers:
        question.answers.append(
            answer_repository.create_answer(text=text, is_true=is_true)
        )

    return question


@pytest.fixture(scope="function")
def answer_repository(test_db_session):
    return AnswerRepository(session=test_db_session)


@pytest.fixture(scope="function")
def user_repository(test_db_session):
    return UserRepository(session=test_db_session)


@pytest.fixture(scope="function")
def user_fixture(user_repository):
    user = user_repository.create_user(name='user_fixture', tg_id=1234)
    return user


@pytest.fixture(scope="function")
def user_answer_repository(test_db_session):
    return UserAnswerRepository(session=test_db_session)
