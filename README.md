\# TIH QA Automation



!\[Python](https://img.shields.io/badge/Python-3.12-blue)

!\[Pytest](https://img.shields.io/badge/Test%20Framework-Pytest-green)

!\[Selenium](https://img.shields.io/badge/UI%20Automation-Selenium-orange)

!\[API Testing](https://img.shields.io/badge/API-Requests-informational)

!\[CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black)



A professional QA automation portfolio demonstrating \*\*UI testing, API testing, data-driven testing, validation, end-to-end testing, test organization, and CI/CD execution\*\* using Python and Pytest.



The project was designed to demonstrate how a maintainable automation framework can be structured for a modern QA engineering environment.



\---



\## Project Overview



This framework covers multiple testing layers:



\* UI automation using Selenium

\* API testing using Python Requests

\* Functional and negative testing

\* Data-driven testing using CSV

\* Customer data validation

\* End-to-end testing

\* Page Object Model architecture

\* Pytest fixtures and configuration

\* Test markers for targeted execution

\* Automated CI execution with GitHub Actions

\* HTML test reporting



The framework is intentionally structured to separate:



\*\*Test cases → Page Objects → API clients → Test data → Configuration → Utilities\*\*



This makes the test suite easier to maintain, extend, and troubleshoot.



\---



\## Technology Stack



| Technology     | Purpose                      |

| -------------- | ---------------------------- |

| Python 3.12    | Test automation language     |

| Pytest         | Test framework               |

| Selenium       | Web UI automation            |

| Requests       | API automation               |

| Git            | Version control              |

| GitHub         | Source control and portfolio |

| GitHub Actions | CI/CD                        |

| CSV            | Test data management         |

| HTML Reporting | Test execution reporting     |



\---



\## Framework Structure



```text

TIH-QA-AUTOMATION/

│

├── .github/

│   └── workflows/

│       └── qa-tests.yml

│

├── api/

│   ├── \_\_init\_\_.py

│   └── customer\_api.py

│

├── app/

│   ├── customer.html

│   ├── index.html

│   └── result.html

│

├── data/

│   └── customers.csv

│

├── pages/

│   ├── base\_page.py

│   ├── customer\_page.py

│   └── quote\_page.py

│

├── tests/

│   ├── test\_api.py

│   ├── test\_customer\_data.py

│   ├── test\_customer\_validation.py

│   ├── test\_end\_to\_end.py

│   └── test\_quote.py

│

├── utils/

│   └── test\_data\_reader.py

│

├── config.py

├── conftest.py

├── pytest.ini

├── requirements.txt

└── README.md

```



\---



\## Testing Scope



\### UI Testing



The UI automation layer uses Selenium and follows a Page Object Model structure.



Tests cover application workflows and validations while keeping page interaction logic separated from test logic.



\### API Testing



The API layer uses Python Requests with a reusable `CustomerAPI` client.



Coverage includes:



\* Successful GET requests

\* Customer data validation

\* HTTP status validation

\* Response structure validation

\* Data type validation

\* Email validation

\* Negative testing

\* Customer creation

\* Parameterized customer testing



\### Data-Driven Testing



Customer test data is maintained separately in CSV format and consumed through a reusable utility.



This demonstrates separation between:



\*\*test logic and test data\*\*



which improves maintainability and makes expanding test coverage easier.



\### End-to-End Testing



End-to-end scenarios validate complete application workflows rather than testing individual components in isolation.



\---



\## Test Organization



Pytest markers are used to organize tests into logical groups.



\### API Tests



```bash

pytest -m api

```



\### Smoke Tests



```bash

pytest -m smoke

```



\### Regression Tests



```bash

pytest -m regression

```



\### Complete Test Suite



```bash

pytest -v --strict-markers

```



\---



\## Test Results



The current automated suite contains:



\*\*20 automated tests\*\*



Latest local regression execution:



```text

20 passed

0 failed

0 skipped

0 errors

```



The project also supports HTML test reporting:



```bash

pytest -v --html=reports/test\_report.html --self-contained-html

```



\---



\## CI/CD



The project includes a GitHub Actions workflow located at:



```text

.github/workflows/qa-tests.yml

```



The pipeline:



1\. Checks out the repository

2\. Sets up Python 3.12

3\. Installs project dependencies

4\. Executes API tests

5\. Executes the complete test suite



This allows automated validation whenever changes are pushed to the main branch or submitted through a pull request.



\---



\## Local Setup



Clone the repository:



```bash

git clone https://github.com/mamabolomalatji91/TIH-QA-AUTOMATION.git

cd TIH-QA-AUTOMATION

```



Create a virtual environment:



```bash

python -m venv .venv

```



Activate it on Windows:



```powershell

.venv\\Scripts\\Activate.ps1

```



Install dependencies:



```bash

pip install -r requirements.txt

```



Run the tests:



```bash

pytest -v --strict-markers

```



\---



\## QA Engineering Practices Demonstrated



This project demonstrates practical experience with:



\* Test automation

\* Functional testing

\* Regression testing

\* Smoke testing

\* Negative testing

\* Boundary and validation testing

\* API testing

\* UI testing

\* End-to-end testing

\* Data-driven testing

\* Page Object Model

\* Pytest fixtures

\* Parameterization

\* Reusable API clients

\* Test data separation

\* Test reporting

\* Git version control

\* GitHub

\* CI/CD

\* Automated test execution



\---



\## Engineering Approach



The framework is designed around three principles:



\### 1. Maintainability



Application interaction logic is separated from test cases through reusable Page Objects and API clients.



\### 2. Reusability



Fixtures, utilities, test data readers, and API methods reduce duplication across the test suite.



\### 3. Continuous Validation



GitHub Actions automatically executes automated tests so that changes can be validated consistently.



\---



\## Future Improvements



Planned improvements include:



\* Enhanced HTML reporting

\* Automated screenshots on UI failure

\* Parallel test execution

\* Browser parameterization

\* Environment-based configuration

\* Improved API schema validation

\* Additional negative and boundary scenarios

\* Dockerized test execution

\* Expanded CI/CD reporting

\* Integration with test management and defect tracking workflows



\---



\## Author



\*\*Mamabolo Malatji\*\*



QA Automation | Python | Selenium | Pytest | API Testing | CI/CD



This repository is part of my QA Engineering portfolio and demonstrates my approach to designing maintainable automated testing solutions.



