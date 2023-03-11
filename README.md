# Django bot server

This is a fork from vaisaghvt/django-bot-server-tutorial which is an accompanying repository for a seminar on creating a django based bot server and also getting started with django-channels. Updated to add 1. Buttons instead of text input 2. PostgreSQL database model to store button clicks per button and per user 3. A simple web page with a table showing number of calls per user. 

# Intro

This is a simple bot that says yo-mama jokes borrowing heavilly from https://github.com/abhay1/django-facebook-messenger-bot-tutorial and the accompanying tutorial. It sets up a bot server that connects Telegram API via webhook and responds to some messages with yo mama jokes.

# Requirements

- Python 2.7
- Make sure you have pip (pip --version)
- pip install virtualenv to install virtual environment
- Telegram messenger (you can also use the web version at web.telegram.org)
- PostgreSQL
- libpq-dev, psycopg2 packages to use python with PostgreSQL (sudo apt install libpq-dev psycopg2)

## What to do

To get this running, you need the following:

### Step 0 : Clone the Repository

`git clone -b F-1 https://github.com/varghese-mannampalli/django-bot-server-tutorial.git`
`cd django-bot-server-tutorial`

### Step 1 : Create a virtual envirnment using python2 and install dependencies

`virtualenv --python="/path/to/python2" "/path/to/new/virtualenv/"`
`source /path/to/new/virtualenv/bin/activate`
`pip install -r requirements.txt`

### Step 2 : Create PostgreSQL role and database, run migrations

Create a PostgreSQL user and database with a login password
Configure Django database settings:
-Update `chatbot_tutorial/settings.py`.
. . .

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

. . .
-Add 'localhost' to ALLOWED_HOSTS in `chatbot_tutorial/settings.py`.
`python manage.py makemigrations`
`python manage.py migrate`
-Create a superuser with:
`python manage.py createsuperuser`

### Step 3 : Start the local server

And start the server with 

`python manage.py runserver`

### Step 4 : Download and use ngrok

You need an HTTPS url for most webhooks for bots to work. For purely development purposes you can use ngrok. It gives a web-accessible HTTPS url that tunnels through to your localhost.
Download ngrok (https://ngrok.com/) , go to a new tab on your terminal and start it with 

`ngrok http 8000`

At this point, you will have to add the URLs to ALLOWED_HOSTS in `chatbot_tutorial/settings.py`.

### Step 5 : Talk to the BotFather and get and set your bot token

Start telegram, and search for the Botfather. Talk to the Botfather on Telegram and give the command `/newbot` to create a bot and follow the instructions to get a token.

Copy the token and paste in `chatbot_tutorial/views.py`

OR

Use the bot that I have created: search for django-channels-bot (the token is already present in `chatbot_tutorial/views.py`)

### Step 6 : Set your webhook by sending a post request to the Telegram API

If you are on a system where you can run a curl command, run the following command in your terminal (Remember to replace ngrok_url and bot_token)

`curl -F -k “url=<ngrok_url>/c817304a3d163ebd58b44dd446eba29572300724098cdbca1a/“ https://api.telegram.org/bot<bot_token>/setWebhook`

Alternatively, you can use some service like Postman or hurl.it just remember to do the following:

- Request type is "POST"
- url to post to https://api.telegram.org/bot<bot_token>/setWebhook
- as parameters add this (name, value) pair: (url, <ngrok_url>/c817304a3d163ebd58b44dd446eba29572300724098cdbca1a/)

You should get a response that states that "webhook has been set"

### Step 7 : Talk to the bot

You should now be able to talk to the bot and get responses from it. 

### Step 8 : View the user calls table

The table should be available at: <ngrok_url>/table/ when the server is running


