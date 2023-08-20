def test_create_term(subject_repository, section_repository, term_repository):
    section_data = {
        "section_name": "some_section_name",
        "subject": subject_repository.get_or_create('some_subject_name')
    }

    section = section_repository.get_or_create(**section_data)
    section_repository.session.commit()

    term_data = {
        'name': 'some_term',
        'section': section
    }

    term = term_repository.get_or_create(**term_data)

    # Проверяем, что Subject добавлен успешно
    assert section.id is not None

    # Попытка создать еще один Subject с тем же именем
    duplicate_term = term_repository.get_or_create(**term_data)

    assert duplicate_term is term

    # Проверяем, что в базе данных действительно только один Subject
    terms = term_repository.get_all()
    assert len(terms) == 1
