def test_create_user_answer(some_user, some_question_with_answers,
                            answer_repository, user_answer_repository):
    user_answer = answer_repository.get_answer_by_question_id_and_text(
        question_id=some_question_with_answers.id,
        text="вариант2"
    )

    assert user_answer is not None

    user_answer_repository.create_user_answer(
        question_id=some_question_with_answers.id,
        user_id=some_user.id,
        answer_text=user_answer.text,
        is_correct=user_answer.is_true
    )

    all_user_answers = user_answer_repository.get_all_answer_by_user_id(
        some_user.id)
    assert 1 == len(all_user_answers)
