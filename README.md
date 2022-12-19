# simplex
blog app

## .env
Store sensitive data in the .env file<br>

The .env file will be hidden automatically from the repo because it should contain sensitive information of the project such as the SECRET_KEY.
After cloning the repo go on and follow these steps:
<ul>
 <li>In the root directory of this Project, create a file called <strong>.env</strong></li>
 <li>After creating the file, write the following lines:</li>

 ```bash
1. SECRET_KEY= SECRET_KEY
2. DEBUG=True
```
<li>This should do the trick, try running the server to check for any errors after creating your .env file</li>

 ```bash
python manage.py runserver
```
</ul>

> ***Note*** <strong>Generating Your Own SECRET_KEY</strong>
<p>To generate a new key, use the get_random_secret_key() function present in the django.core.management.utils that returns a 50 character string of random characters.
You can open the python shell by typing this command first to execute the get_random_secret_key</p>
 ```bash
python manage.py shell
```
After opening shell, execute the following code to generate your random key

 ```bash
 >>>from django.core.management.utils import get_random_secret_key
 >>>print(get_random_secret_key())
```
<p>Copy the key generated and place it in your SECRET_KEY variable in the .env file. <em><strong>There should be no whitespace around the variable</strong></em></p>

