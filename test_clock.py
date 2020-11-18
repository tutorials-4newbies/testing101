import pytest

from clock import Clock


def test_api_response_is_being_checling_tea_time_correctly():
    res = Clock.now("est")
    expected_response = "it's 15:00 o'clock in est, teatime!"
    assert res == expected_response, f"Expected response to be {expected_response} but was different: {res}"


# add a test for checking that in another time zone it's not a time for tea

if __name__ == '__main__':
    pytest.main()
