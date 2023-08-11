def test_create_section(subject_repository, section_repository):
    section_data = {
        "section_name": "some_section_name",
        "subject": subject_repository.get_or_create('some_subject_name')
    }

    section = section_repository.get_or_create(**section_data)
    section_repository.session.commit()
    # Проверяем, что Subject добавлен успешно
    assert section.id is not None

    # Попытка создать еще один Subject с тем же именем
    duplicate_section = section_repository.get_or_create(**section_data)

    assert duplicate_section is section

    # Проверяем, что в базе данных действительно только один Subject
    sections = section_repository.get_all()
    assert len(sections) == 1
