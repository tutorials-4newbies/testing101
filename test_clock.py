from clock import Clock

def test_api_is_being_called(mocker):
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 200
            def json(self):
                return {
                    "currentDateTime":"isnow"
                }
        return MockResponse()
    mocker.patch("clock.requests.get", mock_get)
    res = Clock.now("est")
    assert res == "isnow"
