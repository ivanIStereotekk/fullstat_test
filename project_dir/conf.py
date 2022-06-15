import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'my_db',
'USER': os.getenv('PSGR_USER'),
'PASSWORD': os.getenv('PSGR_PASS'),
'HOST': 'localhost',
'PORT': '5432'
},
}

EMAIL_HOST_USER = 'capitan.django@mail.ru'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASS')
DEFAULT_FROM_EMAIL = os.getenv('DEF_EMAIL')

ADMINS = ((os.getenv('ADMIN_NAME'), os.getenv('DEF_EMAIL')),)

CORS_ORIGIN_REGEX_WHITE_LIST = []