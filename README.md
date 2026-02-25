# QA Engineer Test Task

## Overview

This repository contains an automated test suite created a test task for  **QA Engineer** position.

---

## Task Requirements

- Write automated tests for the provided web application
- Use Python with Playwright (or an alternative such as Selenium)
- Implement at least three tests
- Ensure tests are:
  - Reliable
  - Maintainable
  - Scalable
- Provide:
  - Test code
  - A brief explanation of the approach

---

## Tech Stack

- Python
- Playwright
- Pytest

## Selected Approach

In this task I decided to use Page Object pattern, because this is recommended approach to write tests for website UI. BasePage class contains methods and elements, that are available on every page. And child pages inherit them. 

Tests are separated in files by type and by page under test. In future more complex test structure could be implemented, e.g. separate folders for functional, end-to-end, performance tests etc. But for now it is not needed.

Sensitive test data (in this case link to website under test) is stored in .env file. This file is included in .gitignore. When running in CI or when sharing this repository, this link has to be shared separately.

Other type of test data is test customers' information. This is not secret, so it is stored openly. In case if this data becomes sensitive, or if any production data will be used, this information can also be moved to .env file.
To make data management easier, cutomers' information is stored in dataclass in tests/customers.py file. Dataclass allows testers to get information in different formats: as string, containing first and last name, or as list. If need arouses, other parameters can be added.

## How to Run Tests Locally

### 1. Install dependencies

```
pip install -r requirements.txt
playwright install
```

###  2. Provide environment variables

Put .env file in the root folder. File should contain variable
```
LOGIN_PAGE_URL=<URL>
```

###  3. Navigate to tests folder: 

```
cd tests 
```
#### a) to run tests for login page 
```
pytest login_tests.py 
```

#### b) to run end-to-end tests

```
pytest end_to_end_tests.py
```