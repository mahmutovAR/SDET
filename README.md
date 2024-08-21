# SDET2024

Application for testing the **Student Registration Form**  
`https://demoqa.com/automation-practice-form`
***

### Features of Registration Form:
- The fields `First name`, `Last name`, `Gender` and `Mobile` are required.
* The fields `First name`, `Last name`, `Current address` can be filled with spaces, and this data is valid.  
- If one of the fields `Date of birth` or `Subjects` is cleared, the form page crashes (nothing is displayed).
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

## Installation
**Requirements**
* `Python` 3.10 (tested to work with == 3.10.14)  
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
Run `python3 run_sdet2024.py` from `/src`
***


## Tests
Run `pytest` to test the application.

The `pytest-xdist` plugin is used to speed up test execution  
Run `pytest -n auto` to spawn a number of worker processes equal to the number of available CPUs,  
and distributing the tests randomly across them.
***


### Files and directories:
* `src/errors/` exception modules
* `src/pictures/` test pictures
* `src/settings/` plugin modules
* `src/tests/` test modules
* `src/run_sdet2024.py` sdet2024 launcher
* `requirements.txt` required packages  
