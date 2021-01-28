import os

# CANARY
# Variables
API_KEY = 'ycjOzOP5loHPPIbfMW6tA7AreqAlq0z4yqxStxk2B8Iwges581rK5V8kIgg4'
DB_DEFAULT = {
    'ENGINE': 'django.db.backends.postgresql',
    'USER': 'canary_dev',
    'NAME': 'canary_dev',
    'PASSWORD': '#P1q2w3e4r$Infra',
}
GAE_PROJECT = 'canary'
GAE_QUEUES = {

}
if os.getenv('GAE_APPLICATION', None):
    # [PRD] environment
    DEBUG = False
    ACCESS_PRD_DB = True        # Don't change it! Used on views.py

    DB_DEFAULT['HOST'] = ''
else:
    # [DEV] environment
    DEBUG = True
    ACCESS_PRD_DB = False       # Set 'True' to access PRD data (remember to turn GAE proxy on)

    DB_DEFAULT['HOST'] = '127.0.0.1'

    if ACCESS_PRD_DB:
        # [PRD] Database (remember to turn GAE proxy on)
        DB_DEFAULT['PORT'] = '5433'
    else:
        # [DEV] Database
        DB_DEFAULT['PORT'] = '5432'
        DB_DEFAULT['NAME'] = 'canary_dev'
        DB_DEFAULT['USER'] = 'canary_dev'
# ----------

ALLOWED_HOSTS = ['*']

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_lm+8a-)(dc(xvke*%zj$1x4&ar!skzbqi8y5t_3bo4ioekcb!'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'notification',

]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
         'rest_framework.permissions.AllowAny',
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_engine.urls'

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

WSGI_APPLICATION = 'django_engine.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# [START db_setup]
DATABASES = {'default': DB_DEFAULT}
# [END db_setup]


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = 'static'
STATIC_URL = '/static/'
