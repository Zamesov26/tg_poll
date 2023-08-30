def test_create_user(user_repository, user_state_repository):
    user_data = {
        "name": "some_user",
        "tg_id": 1234
    }

    user = user_repository.create_user(**user_data)
    user_state_repository.create(user)
    user_repository.session.add(user)
    user_repository.session.commit()
    assert user.id is not None

    assert 'start' == user.states[0].state
