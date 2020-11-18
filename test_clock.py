from clock import Clock


def test_api_resonse_is_being_handled_correctly():
    res = Clock.now("est")
    assert res == "isnow oclock in est", f"Expected response to be 'isnow oclock est' but was different: {res}"


if __name__ == '__main__':
    test_api_resonse_is_being_handled_correctly()
