def test_create_subject(question_repository, question_type_repository):
    answer_type_data = {
        "name": "some_answer_type"
    }
    answer_type = question_type_repository.get_or_create(**answer_type_data)
    question_type_repository.session.commit()
    assert answer_type.id is not None

    duplicate_subject = question_type_repository.get_or_create(**answer_type_data)

    assert duplicate_subject is answer_type

    answer_types = question_type_repository.get_all_answer_types()
    assert len(answer_types) == 1
