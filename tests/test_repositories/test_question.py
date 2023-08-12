from app.models import Question


def test_create_question(subject_repository, question_repository):
    question_data = {
        "text": "some_question",
        "subject": subject_repository.get_or_create('some_subject')
    }

    subject = question_repository.get_or_create(**question_data)
    question_repository.session.commit()
    assert subject.id is not None

    duplicate_subject = question_repository.get_or_create(**question_data)

    assert duplicate_subject is subject

    subjects = question_repository.session.query(Question).all()
    assert len(subjects) == 1
