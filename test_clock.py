from clock import Clock


def test_api_is_being_called():

    res = Clock.now("est")
    assert res == "isnow"
