"""
Django settings for KPMB project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from pathlib import Path
import os
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# line28 DEBUG = os.environ.get('DJANGO_DEBUG','')!='False'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY)','django-insecure-6wl*oto&&)puyz91ti4=x!l#a^7(2ylwgov12^$jp4&19#x#ay')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG','')!='False'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'studentmodule'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'   
]

ROOT_URLCONF = 'KPMB.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'KPMB.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

STATIC_ROOT = BASE_DIR/'static'
STATIC_URL = 'static/'




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)














"""
buka github, create new repository

                    
gitbash,,,

masuk dalam folder project,
path yang perlu gitbash, file yang before ade manage.py


dalam gitbash,,,
git init
git add .
git commit -m "first commit"
paste code(git remote) dalam github
git push -u origin master

refresh github

bukak pythonanywhere

delete file previous,tekan files,delete file bawah sekali belah kiri(kanan jangan usik) and masuk dalam virtualenv,delete file dalam tu



bash console,
git clone (paste link <>code dalam github)
mkvirtualenv --python=/usr/bin/python3.10 cocuricularite-virtualenv
ls,cd sampai kluar manage.py

bukak web,add new web app
manual configiration
python 3.9


paste cocuricularsite-virtualenv(dalam bash console) ke dalam virtualenv(dalam web app)


buka file wsgi configuration file (ada atas virtualenv)
padam yang dalam tu,copy yangni   ===============================================================

# +++++++++++ DJANGO +++++++++++
# To use your own Django app use code like this:
import os
import sys

# assuming your Django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/myusername/mysite'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

## Uncomment the lines below depending on your Django version
###### then, for Django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
###### or, for older Django <=1.4
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()


Ubah path dalam ni
path = '/home/myusername/mysite'

cara nak tengok path,
dashboard pythonanywhere,click Files,
tekan nama project kiri bawah sekali,
tekan sekali lagi


ada path,copy yangtu
path = '/home/nikfauzan/cocuricular_project/cocuricular'


Tukar jugak 'mysite' dengan project sendiri
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'



bukak bash console balek,,,,
pip install django
pip install -r requirements.txt
python manage.py createsuperuser
masukkan yang dia mintak
pythob manage.py migrate

bukak pythonanywhere,bukak web,,,,
tekan reload,
tekan link yang atas reload tuu


bukak setting.py dalam pythonanywhere and vscode,,,
line 30	ALLOWED_HOSTS = [ 'nikfauzan.pythonanywhere.com']

make sure save and refresh





"""