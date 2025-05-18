# findpkg

`findpkg` is a Python module that provides a utility function `find` to locate an integer `n` within a specified range `[a, b]` such that an increasing function `f(n) = y`. It uses binary search for efficient solving and includes assertions to ensure validity of input and function behavior.

## Features

- Binary search for solving `f(n) = y` within a bounded range.
- Asserts on input range validity and function monotonicity.
- Fully tested with `pytest` under both Python 2.7 and Python 3.x.
- Linting with `flake8` to ensure code quality.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/findpkg.git
cd findpkg
```

###  Python 3 (Recommended)
Install the dependencies and run in Python 3.9+:
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt  # (if you create one) or:
pip install flake8 pytest
```

### Python 2.7 (via Docker)
We use a Docker container to support legacy Python 2.7 testing:
```bash
docker build -f python2.Dockerfile -t py27 .
```

---

## Usage

You can import and use the `find` function as follows:
```python
from findpkg.find import find

def f(n):
    return n * 2

result = find(f, y=10, a=0, b=10)
print(result)  # Output: 5
```

---

## Running Tests

### Python 3
To run all tests and check for lint issues in your current environment:
```bash
flake8 .  # optional linting
pytest
```

### Python 2.7 (via Docker)
To run linting and tests inside the Docker container:
```bash
docker run --rm py27 flake8 /app/findpkg --count --select=E9,F63,F7,F82 --show-source --statistics
docker run --rm py27 flake8 /app/findpkg --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
docker run --rm py27 pytest
```

---

## Continuous Integration

This project is tested using GitHub Actions on:

> * Python 2.7 (in Docker)
> * Python 3.9, 3.10, and 3.11

You can find the CI configuration in `.github/workflows/ci.yml.`
