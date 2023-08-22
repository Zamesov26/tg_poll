<<<<<<< HEAD
def test_create_user_answer_text(user_fixture, text_question_fixture,
                                 user_answer_repository):
    user_answer_repository.create_user_answer(
        question_id=text_question_fixture.id,
        user_id=user_fixture.id,
=======
def test_create_user_answer_text(some_user, some_question_with_answers,
                                 user_answer_repository):
    user_answer_repository.create_user_answer(
        question_id=some_question_with_answers.id,
        user_id=some_user.id,
>>>>>>> 9b3ecbcba4e59beab0b922a44925d6d5923b2f22
        answer_text='Вариант2',
    )

    all_user_answers = user_answer_repository.get_all_answer_by_user_id(
        user_fixture.id)
    assert 1 == len(all_user_answers)


<<<<<<< HEAD
def test_create_user_answer_single(user_fixture, single_question_fixture,
                                   user_answer_repository):
    user_selected = single_question_fixture.answers[0]
    user_answer_repository.create_user_answer(
        question_id=single_question_fixture.id,
        user_id=user_fixture.id,
        answer_lst=[user_selected]
    )

    all_user_answers = user_answer_repository.get_all_answer_by_user_id(
        user_fixture.id
    )
    assert 1 == len(all_user_answers)
    user_answer_repository.session.commit()
    assert 1 == len(all_user_answers[0].selected_answers)


def test_create_user_answer_multiple(user_fixture, multiple_question_fixture,
                                     user_answer_repository):
    user_selected = multiple_question_fixture.answers[:2]
    user_answer_repository.create_user_answer(
        question_id=multiple_question_fixture.id,
        user_id=user_fixture.id,
        answer_lst=user_selected
    )

    all_user_answers = user_answer_repository.get_all_answer_by_user_id(
        user_fixture.id
    )
    assert 1 == len(all_user_answers)
    user_answer_repository.session.commit()
    assert 2 == len(all_user_answers[0].selected_answers)
=======
def test_create_user_answer_single():
    assert False, "Тест не реализован"


def test_create_user_answer_multiple():
    assert False, "Тест не реализован"
>>>>>>> 9b3ecbcba4e59beab0b922a44925d6d5923b2f22
