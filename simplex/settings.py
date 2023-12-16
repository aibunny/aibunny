
import os
from pathlib import Path
from dotenv import load_dotenv
from django.core.management.utils import get_random_secret_key

# Database url
import dj_database_url


load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
TIME_ZONE = 'Africa/Nairobi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS =['127.0.0.1','.theaibunny.com','65.0.92.54']


# Application definition

AUTHENTICATION_BACKENDS = [
   
    'django.contrib.auth.backends.ModelBackend',
       
]

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'jazzmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    'corsheaders',
    "django.contrib.staticfiles",
    "django.contrib.sites",    
    "theblog",
    'ckeditor',
    'ckeditor_uploader',
    'hitcount',
    'storages',
    'django_extensions',
    'django.contrib.sitemaps',
    ]

#To show debug logs when in deployment
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # 'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            #'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            #'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
           'OPTIONS': {
            'context_processors': [
               
                'django.template.context_processors.request',
            ],
        },
        
    },
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",    
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
]

ROOT_URLCONF = "simplex.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
            
        },
    },
]

WSGI_APPLICATION = "simplex.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASE_URL = os.getenv("DATABASE_URL")
DATABASES = {
   "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=1800),
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS =[
    os.path.join(BASE_DIR, 'theblog/templates/static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


DEFAULT_FILE_STORAGE = 'simplex.storages.MediaStore'

AWS_QUERY_STRING = False
AWS_ACCESS_KEY_ID =os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY =os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME =os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False


 
 
##### CKEDITOR #################################
CKEDITOR_UPLOAD_PATH ='uploads/'


CKEDITOR_CONFIGS = {
    'default' : {
           'extraPlugins': ','.join([
            'uploadimage', # the upload image feature
            # your extra plugins here
            'codesnippet',
            'autolink',
            'autoembed',
            'embedsemantic',
            'scayt',
    
            
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath'
        ]),
        'toolbar' : 'full',
        'height': '700',
    }, 
    
}


STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

#Sitemaps

SITEMAP_MAPPING = 'urls.sitemaps'
SITEMAP_INDEX_NAME = 'sitemap-index'
SITEMAPS_VIEW_NAME = 'django.contrib.sitemaps.views.sitemap'



## HTTPS settings

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    'https://*.theaibunny.com',
    'http://65.0.92.54','http://127.0.0.1:8000']



CORS_ALLOWED_ORIGINS = [
    'https://*.theaibunny.com',
    'http://65.0.92.54','http://127.0.0.1:8000']
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_METHODS = [    'GET',    'POST',    'PUT',    'PATCH',    'DELETE',    'OPTIONS']
CORS_ALLOWED_HEADERS = [    'accept',  
                        'accept-encoding',  
                        'authorization',  
                        'content-type',
                        'dnt',    'origin', 
                        'user-agent', 
                        'x-csrftoken',  
                        'x-requested-with']
CORS_ORIGIN_WHITELIST = [
    'https://*.theaibunny.com',
    'http://65.0.92.54','http://127.0.0.1:8000']
CORS_ORIGIN_ALLOW_ALL = True

print("""
      **************
        **********
          ******
            **
            *
      """
      )