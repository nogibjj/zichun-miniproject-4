# Mini Project 4

This project sets up a CI/CD pipeline using GitHub Actions to test Python scripts across multiple Python versions and operating systems (Ubuntu and Windows).

## CI/CD Status

![CI](https://github.com/nogibjj/zichun-miniproject-4/actions/workflows/ci.yml/badge.svg)

## How to run the project locally

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run tests

```bash
pytest test_main.py
```

## Project Structure

- `main.py`: Contains the `os_and_sys_version` function, which returns the current Python version and OS.
- `test_main.py`: Contains tests for the `os_and_sys_version` function.
- `.github/workflows/ci.yml`: GitHub Actions workflow for running tests on multiple OS and Python versions.

## CI/CD

The CI/CD pipeline runs the following:
- Tests across 3 Python versions: 3,7, 3.8, 3.9, 3.10 and 3.11.
- Tests on both Ubuntu and Windows environments.

Make sure to check the CI status badge to ensure that the latest build has passed.
