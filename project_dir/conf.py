import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['localhost','127.0.0.1','*']

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': os.getenv('POSTGRES_NAME'),
'USER': os.getenv('POSTGRES_USER'),
'PASSWORD': os.getenv('POSTGRES_PASS'),
'HOST': os.getenv('POSTGRES_HOST'),
'PORT': '5432'
},
}

EMAIL_HOST_USER = 'capitan.django@mail.ru'
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASS')
DEFAULT_FROM_EMAIL = os.getenv('DEF_EMAIL')

ADMINS = ((os.getenv('ADMIN_NAME'), os.getenv('DEF_EMAIL')),)

CORS_ORIGIN_REGEX_WHITE_LIST = []