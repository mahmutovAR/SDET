# SDET2024

Application for testing the **Student Registration Form**
`https://demoqa.com/automation-practice-form`
***

## Installation
**Requirements**
* `Python` 3.10 (tested to work with == 3.10.14)  
* `beautifulsoup4` (tested to work with == 4.12.3)  
* `configparser` (tested to work with == 7.0.0)  
* `selenium` (tested to work with == 4.23.0)  
* `pytest` (tested to work with ==8.3.1)  
* `selenium` (tested to work with == 4.23.0)  
* `lxml` (tested to work with == 5.2.2)  

**Note:** The packages can be installed by running `python3 -m pip install -r requirements.txt`
***

### Set FORM URL
#### as Environment Variable
In `bash` run:
```
export PRACTICE_FORM_URL="https://demoqa.com/automation-practice-form"
```
In `Python Console` run:
```
from os import environ
environ['PRACTICE_FORM_URL'] = 'https://demoqa.com/automation-practice-form'
```
#### as key `url` in sections `PRACTICE_FORM_URL` in 'form_data.ini'
```
[PRACTICE_FORM_URL]
url = https://demoqa.com/automation-practice-form
```
***

## Quick Start Guide (in progress..)
1. Run the `create_sample.py` script.  
It will create the `form_data.ini` file with sample form data.
2. Then, run the `run_sdet2024.py` script.  
***

## Running SDET2024
* create `form_data.ini`
* run `python3 run_sdet2024.py`
***

### The `form_data.ini` file contains the next data

**First Name** and **Last Name** string data  
**Email** email format, name@example.com   
**Gender** `male` `female` `other`  
**Mobile** 10 digits only  
**Date of birth** valid date in format `dd mm yyyy` `dd-mm-yyyy` `dd.mm.yyyy` `dd,mm,yyyy` `dd/mm/yyyy`  
**Subjects** `Accounting` `Arts` `Biology` `Chemistry` `Civics`,
            `Commerce` `Computer Science` `Economics` `English` `Hindi`
            `History` `Maths` `Physics` `Social Studies`  
**Hobbies** `sports`, `reading`, `music`
**Picture** valid file
**Current Address** string format  
**Select State** and **Select City** `NCR`: `Delhi`, `Gurgaon`, `Noida`,
              `Uttar Pradesh`: `Agra`, `Lucknow`, `Merrut`,
              `Haryana`: `Karnal`, `Panipat`
              `Rajasthan`: `Jaipur`, `Jaiselmer`

Example of `form_data.ini` file:  
```
[form_data]
url = https://demoqa.com/automation-practice-form

[student_data]
first_name = Joseph David
last_name = Smithsen
email = jd.smithsen@td-kolner.com
gender = male
mobile = 8087971551
birth_date = 29 02 2004
subjects = physics, maths, computer science
hobbies = music, sports
picture = /user/pictures/ebersteiger.jpg
address = Gramin Rd, Kapil Sharad 3451
state = Uttar Pradesh
city = Merrut
```


## Tests
run `pytest` (in progress..)
***

### Files and directories:
- `requirements.txt` required packages  
* `./tests` test module package