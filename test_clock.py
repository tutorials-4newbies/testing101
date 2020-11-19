import pytest

from clock import Clock


def test_api_response_is_checking_tea_time_correctly(mocker):
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 200

            def json(self):
                return {
                    "currentDateTime": "2020-11-18T15:00-05:00"
                }

        return MockResponse()

    mocker.patch("clock.requests.get", mock_get)
    res = Clock.now("est")
    expected_response = "it's 15:00 o'clock in est, teatime!"
    assert res == expected_response, f"Expected response to be {expected_response} but was different: {res}"


# add a test for checking that in another time zone it's not a time for tea

# add a test and then a feature where israel time zone is never time for tea
if __name__ == '__main__':
    pytest.main()
