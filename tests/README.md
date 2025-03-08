# Tests

## Overview
This directory contains unit tests for the Calculate Age application.

## Running Tests
You can run all tests using the test runner:

```bash
python tests/run_tests.py
```

Or run individual test files:

```bash
python -m unittest tests/test_calculations.py
```

## Test Files
- `test_calculations.py`: Tests for the age calculation logic
- `run_tests.py`: Test runner to discover and run all tests

## CI Integration
Tests automatically run on every build through GitHub Actions. The CI workflow is defined in `.github/workflows/ci.yml`.