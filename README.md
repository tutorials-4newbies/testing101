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
