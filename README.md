## PFC case
# Given test scenarios:
http://127.0.0.1:8000/api/?country_code=PK&iban=PK36 SCBL 0000 0011 2345 6702
http://127.0.0.1:8000/api/?country_code=ABC&iban=123456
http://127.0.0.1:8000/api/?country_code=AE&iban=SE45 5000 0000 0583 9825 7466
http://127.0.0.1:8000/api/?country_code=SE&iban=PK45 5000 0000 0583 9825 7466
http://127.0.0.1:8000/api/?country_code=se&iban=SE45 5000 0000 0583 9825 7466
http://127.0.0.1:8000/api/?country_code=VA&iban=VA59001123000012345678
http://127.0.0.1:8000/api/?country_code=SE&iban=SE4550000000058398257466
http://127.0.0.1:8000/api/?country_code=SE&iban=SE4550000000058398257900


# Steps
# Open shell/terminal and run following command to clone the project:
- git clone https://github.com/hamzafaisaljarral/IBANvalidator
# Versions
- python3 and pip3 are installed .
 
# run the project
- cd IBANvalidator
- source venv/bin/activate

- pip3 install -r requirments.txt

- python3 manage.py migrate
- python3 manage.py runserver 8000


- Here are the URLs for 8 mentioned scenarios: 1. http://127.0.0.1:8000/api/?country_code=SE&iban=PK45 5000 0000 0583 9825 7466


# Tests
Following command can be used to run test cases:
-python manage.py test

## Docker setup
# Clone my repo
- git clone https://github.com/hamzafaisaljarral/IBANvalidator

# Make sure docker is installed on your system and run following commands inside your project directory:
- sudo docker-compose build
- sudo docker-compose up

# Validation API is deployed on Heroku as well for testing

https://ibanvalidatorforbank.herokuapp.com/api/?country_code=SE&iban=PK45 5000 0000 0583 9825 7466



<img width="1440" alt="Screen Shot 2022-05-03 at 5 57 32 AM" src="https://user-images.githubusercontent.com/39766112/166394361-3c352ef9-9a95-43a5-acce-32c795c5cd09.png">

