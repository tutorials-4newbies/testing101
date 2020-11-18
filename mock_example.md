```python
    # add mocker to function parameters
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 200

            def json(self):
                return {
                    "currentDateTime": "isnow"
                }

        return MockResponse()

    mocker.patch("clock.requests.get", mock_get)

```