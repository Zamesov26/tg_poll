def test_create_answer(answer_repository):
    answers_data = [("Один", True), ("Два", False), ("Три", False)]
    for text, is_true in answers_data:
        answer_repository.create(text=text, is_true=is_true)

    lst = answer_repository.get_all_answer()
    assert 3 == len(lst)
