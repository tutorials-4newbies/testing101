```python
    # add mocker to function parameters
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 200

            def json(self):
                return {
                    "currentDateTime": "2020-11-18T15:00-05:00"
                }

        return MockResponse()

    mocker.patch("clock.requests.get", mock_get)

```