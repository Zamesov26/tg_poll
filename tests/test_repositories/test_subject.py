from app.models import Subject


def test_create_subject(subject_repository):
    subject_data = {
        "name": "Math"
    }
    subject = subject_repository.get_or_create(**subject_data)
    subject_repository.session.commit()
    # Проверяем, что Subject добавлен успешно
    assert subject.id is not None

    # Попытка создать еще один Subject с тем же именем
    duplicate_subject = subject_repository.get_or_create(**subject_data)

    assert duplicate_subject is subject

    # Проверяем, что в базе данных действительно только один Subject
    subjects = subject_repository.session.query(Subject).all()
    assert len(subjects) == 1
