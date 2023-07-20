"""
Django settings for crashblog project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
import dj_database_url

from pathlib import Path
from dotenv import load_dotenv

load_dotenv()       #loadind env variables



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Mq0ZMZTThad2KzSF0eEyQjz05I363DUIVNgWdbSXDubP5vlQ8d' #os.environ.get('Crashblog_Secret_key')

# SECURcd ITY WARNING: don't run with debug turned on in production!
DEBUG = True #(os.environ.get('DEBUG'  == 'TRUE'))

ALLOWED_HOSTS = ['tobietopia.vercel.app', '.now.sh','tobietopia.fly.dev', 'localhost',
                 '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://tobietopia.vercel.app','https://tobietopia.fly.dev', 'https://localhost',]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig' ,         #core here is name of our app,app is the file inside of core called app.py and  coreconfig is the name of our class in the app.py    
    'blog.apps.BlogConfig',             #our blog app
    'crashblog',
    'taggit',
    'ckeditor',
    'ckeditor_uploader', 
    'django_social_share',
    'whitenoise',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],              # telling django wherev to look for our templates files, so make sure in folder we name where we store our templates as templates
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

WSGI_APPLICATION = 'crashblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': dj_database_url.parse('postgres://tobietopia:VodIUSAAt1EZF5ELDwRf9bqmU2CNIADl@dpg-cisqfg18g3n42ohd5hc0-a.oregon-postgres.render.com/tobietopia'),
}

#Test DB
''''default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Tobietopia',
        'USER': 'postgres',
        'PASSWORD': 'mattew50',
        'HOST': 'localhost',
        'PORT': '5432',
    }'''




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'            #this is where all our media files will be stored, remember to pip install pillow for handling image
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#CKEDITOR Rich Text format
def static_font(path):
    from django.templatetags.static import static
    from django.utils.functional import lazy

    return lazy(lambda: static(path), str)()

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'


CKEDITOR_CONFIGS = {

    'default': {
        'toolbar': 'full',
        'format_tags': 'h1;h2;h3;p;pre',
        'toolbar_Custom': [
            
            ['Format', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            ['Source', 'Undo', 'Redo'],
        ],
        'contentsCss': [static_font('css/font.css')],
    }
}


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#Email settings
EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '75faeb277b4853' #os.environ.get('host')
EMAIL_HOST_PASSWORD = '879df8d7b8ade8' #os.environ.get('host_pass')
EMAIL_PORT = '2525'

