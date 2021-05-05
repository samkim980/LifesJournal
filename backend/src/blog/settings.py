from pathlib import Path

import os

import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG == True:
    SECRET_KEY = '%b8uo-#4lms4y$_2!n#aupiww-1n2&+1makxo*f=j(i87p-emn'
else:
    SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',
    'storages',
    'ckeditor',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'
# os.path.join(BASE_DIR, 'build')
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

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


CKEDITOR_UPLOAD_PATH = 'uploads/'



STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn", "static_root")

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'build/static'),
    os.path.join(BASE_DIR, 'static'),
]


# Path where media is stored
MEDIA_ROOT = os.path.join(BASE_DIR, "static_cdn", "static_media")
MEDIA_URL = '/media/'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


REST_FRAMEWORK = {
     'DEFAULT_PERMISSION_CLASSES': (
         'rest_framework.permissions.IsAuthenticated',
     ),
     'DEFAULT_AUTHENTICATION_CLASSES': (
         'rest_framework.authentication.SessionAuthentication',
         'rest_framework.authentication.BasicAuthentication',
         'rest_framework.authentication.TokenAuthentication',
     ),
 }


CORS_ORIGIN_ALLOW_ALL=True

CORS_ORIGIN_WHITELIST = [
    'https://localhost:3000',
]


# Activate Django-Heroku.
django_heroku.settings(locals())
