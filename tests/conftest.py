import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Base
from app.repositories import (SubjectRepository, SectionRepository,
    TermRepository, QuestionRepository)


@pytest.fixture(scope="function")
def test_db_session():
    engine = create_engine(
        "sqlite:///:memory:")  # Создание SQLite in-memory базы данных
    Session = sessionmaker(bind=engine)
    session = Session()

    # Создайте структуру базы данных (например, выполнив create_all())
    Base.metadata.create_all(engine)

    yield session

    session.close()


@pytest.fixture(scope="function")
def subject_repository(test_db_session):
    return SubjectRepository(session=test_db_session)


@pytest.fixture(scope="function")
def section_repository(test_db_session):
    return SectionRepository(session=test_db_session)


@pytest.fixture(scope="function")
def term_repository(test_db_session):
    return TermRepository(session=test_db_session)


@pytest.fixture(scope="function")
def question_repository(test_db_session):
    return QuestionRepository(session=test_db_session)
