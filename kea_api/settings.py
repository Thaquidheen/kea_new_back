# Clean Django settings.py - Normal Configuration

from pathlib import Path
from datetime import timedelta
import os
# import os

from django.core.management.utils import get_random_secret_key
import dj_database_url

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY SETTINGS
RAZORPAY_KEY_ID = os.environ.get("RAZORPAY_KEY_ID", "")
RAZORPAY_KEY_SECRET = os.environ.get("RAZORPAY_KEY_SECRET", "")

# Generate a secret key if not in environment
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_secret_key())

# Debug setting
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# ALLOWED_HOSTS
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'web-production-c00c.up.railway.app',
    '.railway.app',
]

FRONTEND_URL = 'https://keablrfrotend.netlify.app'

# CORS Settings - Simple and Clean
CORS_ALLOWED_ORIGINS = [
    "https://keablrfrotend.netlify.app",
    "http://localhost:3000",
    "https://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# CSRF Settings
CSRF_TRUSTED_ORIGINS = [

    "https://web-production-c00c.up.railway.app",
    "https://keablrfrotend.netlify.app",
    "http://localhost:3000",
]

# SSL Settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static and Media files
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files - use Railway volume path
# For Railway deployment - use volume path
if os.environ.get('RAILWAY_ENVIRONMENT'):
    # Railway volume path
    MEDIA_ROOT = '/app/media'
else:
    # Local development
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Ensure media directory exists
import os
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT, exist_ok=True)

# Email configuration

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'thaquidheen@gmail.com'
EMAIL_HOST_PASSWORD = 'mxip pyxb jrud xfyw' 
DEFAULT_FROM_EMAIL = 'thaquidheen@gmail.com'



# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Application definition
INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'userdata',
    'programdata',
]

# Middleware - Standard order
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Production Security Settings
if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# URLs and WSGI
ROOT_URLCONF = 'kea_api.urls'
WSGI_APPLICATION = 'kea_api.wsgi.application'

# Custom User Model
AUTH_USER_MODEL = 'userdata.CustomUser'

# Authentication Backends
AUTHENTICATION_BACKENDS = [
    'userdata.auth_backend.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DATABASE_NAME', 'railway'),
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE_PORT', '41172'),
        'OPTIONS': {
            'sslmode': 'require',
        }
    }
}
# Database configuration
DATABASE_URL = os.environ.get('DATABASE_URL')
# DB_LIVE = os.getenv("DB_LIVE")

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL)
    }

 
# elif DB_LIVE in ["False", False]:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }
# else:
    
#     DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.postgresql'),
#         'NAME': os.environ.get('DATABASE_NAME', 'railway'),
#         'USER': os.environ.get('DATABASE_USER', 'postgres'),
#         'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
#         'HOST': os.environ.get('DATABASE_HOST', 'localhost'),
#         'PORT': os.environ.get('DATABASE_PORT', '41172'),
#         'OPTIONS': {
#             'sslmode': 'require',
#         }
#     }
# }

# Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# JWT Configuration
SIMPLE_JWT = {
    "USER_ID_FIELD": "user_id",
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': os.environ.get("JWT_SIGNING_KEY", SECRET_KEY),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Admin configurations
ADMIN_SITE_HEADER = "Kerala Engineers Association Admin"
ADMIN_SITE_TITLE = "KEA Administration"
ADMIN_INDEX_TITLE = "Membership Management"

# Additional settings
X_FRAME_OPTIONS = 'SAMEORIGIN'
SILENCED_SYSTEM_CHECKS = ['security.W019']


# QR Code encryption key
QR_ENCRYPTION_KEY = os.environ.get('QR_ENCRYPTION_KEY', SECRET_KEY[:32])

# Secret key for JWT signing of QR codes
QR_JWT_SECRET = os.environ.get('QR_JWT_SECRET', SECRET_KEY[:32])

# QR code expiration time (1 year by default)
QR_CODE_EXPIRY = timedelta(days=365)

SITE_URL = os.environ.get('SITE_URL', 'https://keablrfrotend.netlify.app')
# Simple logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}