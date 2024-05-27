# Unittests and Integration Tests

## Overview

This project focuses on unit and integration testing for Python applications. The goal is to ensure that individual components (functions and methods) work as expected in isolation (unit tests) and that the system works as a whole (integration tests).

## Learning Objectives

By the end of this project, you should be able to:
- Understand the difference between unit and integration tests.
- Implement common testing patterns such as mocking, parametrizations, and fixtures.

## Unit Tests

Unit testing involves testing individual functions or methods to verify their correctness. Unit tests should cover:
- Standard inputs and corner cases.
- Only the logic defined within the function being tested.
- Mocking of external dependencies, especially those making network or database calls.

The main question answered by unit tests is: **If everything defined outside this function works as expected, does this function work as expected?**

OOA## Integration Tests

Integration testing involves testing a complete code path end-to-end. These tests:
- Verify interactions between different parts of the system.
- Mock only the low-level functions that make external calls (HTTP requests, file I/O, database I/O).

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7).
- Files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- Follow the `pycodestyle` style (version 2.5).
- All files must be executable.
- All modules, classes, and functions should have comprehensive documentation.
- All functions and coroutines must be type-annotated.

## Running Tests

Execute your tests with the following command:
```bash
$ python -m unittest path/to/test_file.py
