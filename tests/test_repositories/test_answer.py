def test_create_answer(answer_repository):
    answers_data = [("Один", True), ("Два", False), ("Три", False)]
    for text, is_true in answers_data:
<<<<<<< HEAD
        answer_repository.create_answer(text=text, is_true=is_true)

    lst = answer_repository.get_all_answer()
    assert 3 == len(lst)
=======
        answer = answer_repository.create_answer(text=text, is_true=is_true,
                                                 **general_answers_data)
        some_question.answers.append(answer)

    lst = answer_repository.get_all_answer()
    print(lst)
    assert len(some_question.answers) == 3
>>>>>>> 9b3ecbcba4e59beab0b922a44925d6d5923b2f22
