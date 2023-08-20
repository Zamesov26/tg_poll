def test_create_subject(subject_repository):
    subject_data = {
        "name": "Math"
    }
    subject = subject_repository.get_or_create(**subject_data)
    subject_repository.session.commit()

    assert subject.id is not None

    duplicate_subject = subject_repository.get_or_create(**subject_data)

    assert duplicate_subject is subject

    subjects = subject_repository.get_all()
    assert len(subjects) == 1
