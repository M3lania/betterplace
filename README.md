# BetterPlace.org


 Introduction
---
BetterPlace is a suite of Selenium automated tests for [BetterPlace.org](https://betterplace.org).


Running the tests locally
---

* System requirements:
  * python 3
  * pip
  * Google Chrome
  * [ChromeDriver](https://sites.google.com/chromium.org/driver/)

* Clone this repo

* Since the tests run with CHROME, chromedriver should be downloaded. In order to run the tests, the following argument 
  is required: 
  
      --chromedriver=/path/to/chromedriver 
  
* Next, create and activate a virtual environment:

       virtualenv ve-betterplace -p python3.7
       source ve-betterplace/bin/activate

* Install packages and project dependencies:

      cd betterplace
      pip install -r requirements.txt

* Run all tests or a certain test:
  
       pytest -v -s --chromedriver=/path/to/chromedriver
       pytest -v -s --crhomedriver=/path/to/chromedriver -k test_ui_of_payment_methods
