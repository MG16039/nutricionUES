"""
Django settings for nutricion project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Identificando la ruta del proyecto
import os
from django.core.urlresolvers import reverse_lazy
RUTA_PROYECTO = os.path.dirname(os.path.dirname(__file__))

import sys


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aurnk#+#0#eyx-20z$uhdksn&efusn*kdkr0#j!zu6s-8k*gmi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

ADMINS = (
     ('Monica Castillo', 'monicastilloh9@gmail.com'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.consulta',
    'apps.dieta',
    'apps.login',
    'apps.nutricionista',
    'apps.paciente',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nutricion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(RUTA_PROYECTO, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors':[
                'django.template.context_processors.debug'
                'django.template.context_processors.request'
                'django.contrib.auth.context_processors.auth'
                'django.contrib.messages.context_processors.messages'
            ]
        }
    }
]

TEMPLATE_DIRS = (
    os.path.join(RUTA_PROYECTO, 'templates'),
)

WSGI_APPLICATION = 'nutricion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.mysql',
       #'ENGINE': 'django.db.backends.sqlite3',
       #'NAME': os.path.join(RUTA_PROYECTO, 'db.sqlite3'),
        'NAME': 'nutriciondb',
        'USER': 'root',
        'PASSWORD' : '123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-SV'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#encoding:utf-8

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#Para el login
#LOGIN_REDIRECT_URL = reversed_lazy('paciente:registarPaciente')'/'

#STATICFILES_DIRS = (os.path.join(RUTA_PROYECTO, 'statics'))
