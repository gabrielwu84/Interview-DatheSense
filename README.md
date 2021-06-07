# Introduction
A Django REST API backend of system that is able to save files and analyze the files' sensitivity score. 

Project uses the following containers:
- Postgres container as RDBMS
- redis container for MQ
- Celery container to compute sensitivity score asynchronously
- Web container
- Test container

# Prerequisites
1. docker, docker-compose are installed
2. ports 6379 and 8000 are free

# Installation
1. after unzipping the file, 
2. cd into directory
3. run commands in this sequence - 
```
docker-compose build
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose up
```

# Tests
Successful `docker-compose up` execution should conclude with 
```
test_1    | ...........
test_1    | ----------------------------------------------------------------------
test_1    | Ran 11 tests in 2.430s
test_1    | 
test_1    | OK
test_1    | Destroying test database for alias 'default'...
dathena_v11_test_1 exited with code 0
```
## Test Cases
Test cases/code can be found in folders `./tests/`, and `./sensitive_calc/tests.py`

They include -
*happy flows:*
```
test_user_can_register_correctly
test_file_can_login_correctly
test_file_can_upload_correctly
test_can_list_files_correctly
```
*negative tests:*
```
test_user_cant_register_with_no_data
test_file_cant_upload_without_authentication
test_file_cant_upload_with_wrong_ext
test_cant_list_files_with_wrong_token
```
and 3 unit tests for the sensitivity score algorithm.

## Re-run Tests
Tests can be re-run with 
```
docker-compose run web python manage.py test
```

## Postman
REST API tests can be manually with Postman. 

The following end points are available for testing: 
- POST http://127.0.0.1:8000/api/account/register 
- POST http://127.0.0.1:8000/api/account/login
- POST http://127.0.0.1:8000/api/file/upload 
- GET http://127.0.0.1:8000/api/file/list 
- GET http://127.0.0.1:8000/api/file/list?page=2 

To make request as an authenticated user, first retrieve authentication the token from the return value of a registeration or login, or from the Tokens table admin panel. 

Then fill in the token into the Postman request as an "Authorization" field in Headers. The value of the "Authorization" is of the form "Token <Token>". E.g. Token ec3288c4caf3f4bc14af0c0949838d27d2abf301.

# Admin View
Admin panel can be reached at http://127.0.0.1:8000/admin

Login with superuser that can be created with this command (executed in project directory) -
```
docker-compose run web python manage.py createsuperuser
```

# Other Gotcha's 
1. `docker`, `docker-compose` commands might require `sudo`
2. after executing `manage.py startapp` as `sudo`, may require `sudo chown -R $USER:USER .`.
