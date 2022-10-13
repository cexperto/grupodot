
# palindrome API

Rest API for find palindrome


## Authors

- [@cexperto](https://github.com/cexperto)

  
## Deployment

To deploy this project:

run in bash for agile the process:

```bash
./cli

```

```bash
  python -m venv venv
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  py manage.py runserver
```

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Tech Stack

**Client:** postman, insomnia

**Server:** python, Django, Django REST Framework

  
## API Reference

#### add user 

```http
Post /api/auth/signup/
```
body:
Json exaple
{
	"email": "tmytest2@mail.com",
	"username":"tmytest2",	
	"password":"Ijhgfdsa1$",
	"confirm":"Ijhgfdsa1$"
}
#### login

```http
Post /api/token/
```
body:
Json exaple
{	
	"username":"test",	
	"password":"Ijhgfdsa1$",
	"confirm":"Ijhgfdsa1$"
}
Response status 200
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMTQ0MzA5MSwianRpIjoiOTIxZjY4ZDI1ZTE2NGU5Yzk2OTY4ODU0MjIyNjI3ZTAiLCJ1c2VyX2lkIjoyfQ.8QMdpo274hdJ6tre_Ax8WOZA544GXfZbVIh8lDwF_AQ",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMxMzU2OTkxLCJqdGkiOiI2MGMyNTc4YTA1OGY0MWExOTA5OWE5NjZhMzRlNWI4OCIsInVzZXJfaWQiOjJ9.ImDcvLMfVjB10xElXtxwRAaZaqUoUlMUoBmUnUvHUZ8"
}


 
#### Delete a user
Delete /user/<int>/
just user authenticated
headers :
Authorization : Bearer <token>
Response
{
    "message": "delete success"
}

### get all users
Get /allUsers/

#### find palindrome endpoint
/palindrome
just user authenticated
headers :
Authorization : Bearer <token>
method: POST
request = {
    'text': 'Anita lava la tina'
}

Response
{
	"the palindrome most long the text: ": "12321"
}

#### for run all tests

```bash
    python manage.py test

```
