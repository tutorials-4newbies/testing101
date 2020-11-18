## Unit Testing in python  introductory workshop

## Setup

create a virtualenv
linux 
```bash

python -m venv venv
source testing_venv/bin/activate

```

windows

```
python -m venv venv
testing_venv\Scripts\activate
```

After that
```bash
pip install -r requirements.txt
```

## We'll do a test driven development of a phone number validator

1. validate a cell phone
2. Valid prefixes
3. Handle - separators
4. Handle optional zero
5. Handle optional leading country code
6. Handle DIAL BY ALHPANUMERIC 


## Branches

1. master - unittesting
2. mock - mocking
3. spies - using spy
4. time_travel

## Libraries

* [freeze gun](https://github.com/spulec/freezegun)
* [pytest](https://docs.pytest.org/en/stable/)
* [pytest mocker](https://pypi.org/project/pytest-mock/)
* [python builtin mock](https://docs.python.org/3/library/unittest.mock.html)
* [unittest in python](https://docs.python.org/3/library/unittest.html)

## Read more

* [Google testing blog](https://testing.googleblog.com/)