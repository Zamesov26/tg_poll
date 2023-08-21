def test_create_question(some_subject, question_repository):
    question_data = {
        "text": "some_question1",
        "subject":  some_subject,
        "question_type": 'text'
    }

    question = question_repository.get_or_create(**question_data)
    question_repository.session.commit()
    assert question.id is not None


def test_create_multiple_questions(some_subject, question_repository):
    question_data = {
        "subject": some_subject
    }

    question_texts = ["some_question1", "some_question2"]
    for text in question_texts:
        question_repository.get_or_create(text=text, **question_data)

    questions = question_repository.get_all()
    assert len(questions) == 2


def test_create_duplicate_question(some_subject, question_repository):
    question_data = {
        "subject": some_subject
    }

    question_texts = ["some_question1", "some_question1"]
    for text in question_texts:
        question_repository.get_or_create(text=text, **question_data)

    questions = question_repository.get_all()
    assert len(questions) == 1
