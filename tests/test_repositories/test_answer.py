def test_create_answer(answer_repository, some_question):
    general_answers_data = {
        "question_id": some_question.id,
    }

    answers_data = [("Один", True), ("Два", False), ("Три", False)]
    for text, is_true in answers_data:
        answer_repository.create_answer(text=text, is_true=is_true,
                                        **general_answers_data)

    assert len(some_question.answers) == 3

    # answer_repository.session.commit()
