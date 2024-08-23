# SDET2024

Application for testing the **[Student Registration Form](https://demoqa.com/automation-practice-form)**  
***

### Registration Form features:
- The `First name`, `Last name`, `Gender` and `Mobile` fields are required.
* The `First name`, `Last name` and `Current address` fields can be filled with spaces, and this data is valid.  
- If `Date of birth` or `Subjects` field is cleared, the form page crashes (nothing is displayed).
* After sending the form, the `Close` button is available, after clicking on which the form fields become empty.  
But new data is entered incorrectly, some of it is not displayed in the pop-up window with the entered data.
- If the state in the `Select state` field is selected, but the city in the `Select city` field is not,  
then the `State and city` value in the popup window is empty.
* There are two ways to enter `Date of Birth`:  
    * select a date via the pop-up calendar  
    * enter the date in the `Date of birth` field  
* In the second case, there are some restrictions:
    * if the month is specified as a numeric value, the date must have the format `yyyy mm dd` or `mm dd yyyy`
    * if the month is specified as a string value, the date format is not important
***

## Requirements
To use the application, you must have [Python 3](https://www.python.org/downloads/) 
and [Allure](https://allurereport.org/docs/install/) installed on your operating system.  
`Python` (tested to work with == 3.10.14)  
`Allure` (tested to work with == 2.30.0)

**Python packages**
* `allure-pytest` (tested to work with ==2.13.5)  
* `beautifulsoup4` (tested to work with == 4.12.3)  
* `selenium` (tested to work with == 4.23.0)  
* `pytest` (tested to work with ==8.3.1)  
* `pytest-xdist` (tested to work with ==3.6.1)  
* `rstr` (tested to work with ==3.2.2)  
* `selenium` (tested to work with == 4.23.0)  
* `lxml` (tested to work with == 5.2.2)  

**Note:** The packages can be installed by running `python3 -m pip install -r requirements.txt`
***


## Running SDET2024
Run `run_sdet2024.py` from `/src`  
The form fields will be filled with generated valid data,
then the submitted data will be displayed and scraped for verification
***


## Tests
To test the application and get test report run `sdet2024_testing.py` from `/src`

The `pytest-xdist` plugin extends `pytest` to speed up test execution,  
and `allure-pytest` is used for visualizing the results of a test run.
***


### Files and directories:
- `src/allure-report/index.html` allure report
- `src/allure_files/` test results directory  
**Note:** Allure report files will be generated after running `sdet2024_testing.py`

* `src/errors/` exception modules
* `src/pictures/` test pictures
* `src/settings/` plugin modules
* `src/tests/` test modules
* `src/run_sdet2024.py` sdet2024 launcher
* `src/sdet2024_testing.py` tests launcher
* `task/SDET_2024.pdf` task description
* `requirements.txt` required packages
