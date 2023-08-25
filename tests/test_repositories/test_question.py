def test_create_text_question(question_repository):
    question = question_repository.create(text="test_question_1",
                                          question_type='text')
    question_repository.session.commit()
    assert question.id is not None


def test_create_multiple_questions(question_repository):
    question_texts = ["test_question1", "test_question2"]
    for text in question_texts:
        question_repository.create(text=text, question_type='single_choice')

    questions = question_repository.get_all()
    assert 2 == len(questions)


def test_create_duplicate_question(question_repository):
    question_texts = ["test_question1", "test_question1"]
    for text in question_texts:
        question_repository.create(text=text, question_type='multiple_choice')

    questions = question_repository.get_all()
    assert 2 == len(questions)
