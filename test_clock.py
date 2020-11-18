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


# Now, since the api is costly, we want to cache the results, and the tests should verify it's actually caching

def test_api_is_not_being_called_twice_for_specific_timezone(mocker):
    res = Clock.now("est")
    expected_response = "it's 15:00 o'clock in est, teatime!"

    res = Clock.now("est")
    expected_response = "it's 15:00 o'clock in est, teatime!"

    # Hmm but how can we verify that it's not called twice? 

if __name__ == '__main__':
    pytest.main()
