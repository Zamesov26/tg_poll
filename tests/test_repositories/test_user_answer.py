def test_create_user_answer_text(some_user, some_question_with_answers,
                                 user_answer_repository):
    user_answer_repository.create_user_answer(
        question_id=some_question_with_answers.id,
        user_id=some_user.id,
        answer_text='Вариант2',
    )

    all_user_answers = user_answer_repository.get_all_answer_by_user_id(
        some_user.id)
    assert 1 == len(all_user_answers)


def test_create_user_answer_single():
    assert False, "Тест не реализован"


def test_create_user_answer_multiple():
    assert False, "Тест не реализован"
