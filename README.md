# QA Engineer Test Task

## Overview

This repository contains an automated test suite created a test task for  **QA Engineer** position.

---

## Task Requirements

> Task: Write a few automated tests for the following site https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login
> 1. Use Python with playwright (or any alternative such as Selenium). 
> 2. Write a minimum of three tests 
> 3. Make sure that the tests are reliable, maintainable, and scalable. 
> 4. Share us the code and a brief explanation of your approach. 
> 5. Please attempt to showcase your automation skills and experience with this task 
> 
> We expect that the task will take you approximately 2-3 hours to complete. Please let us know if you require any further information or have any questions about the task.
---

## Tech Stack

- Python
- Playwright
- Pytest

## Selected Approach

In this task I decided to use Page Object pattern, because this is recommended approach for writing UI tests. BasePage class contains methods and elements that are available on every page, and child pages inherit them.

Tests are separated into files by type and by page under test. In future, more complex structure could be implemented, for example separate folders for functional, end-to-end and performance tests. But for now this is not needed.

Sensitive test data (in this case URL of website under test) is stored in .env file, which is included in .gitignore. When running in CI or when sharing this repository, this value has to be provided separately.

Other test data is customers' information. This is not sensitive, so it is stored openly in the repository. If this changes, or if any production data will be used, it can also be excluded from git.

To make data management easier, customers' information is stored as dataclass in tests/customers.py. This allows to get customer data in different formats — as a full name string or as a list. More fields can be added if needed.

There is also an option to run tests in Github Actions. To trigger tests manually or check past runs, navigate to Actions tab in Github. Tests also run automatically every day at midnight (GMT+0).

## How to Run Tests Locally

### 1. Install dependencies

```
pip install -r requirements.txt
playwright install
```

###  2. Provide environment variables

There are two methods to do it:

a) Put .env file in the root folder. File should contain variable ***LOGIN_PAGE_URL=< URL >***

b) Put the same variable in run configuration in your IDE.


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

