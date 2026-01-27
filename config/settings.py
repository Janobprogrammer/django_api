import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv("C:/Users/user/Desktop/django_api/.env")

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True
APPEND_SLASH = True

ALLOWED_HOSTS = ["*"]

# ALLOWED_HOSTS = [
#     "interapis.uz",
#     "www.interapis.uz"
# ]

CSRF_TRUSTED_ORIGINS = [
    "https://themeless-constance-zoomorphic.ngrok-free.dev",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "django_filters",
    'drf_yasg',

    # Local apps
    "accounts.apps.AccountsConfig",
    "flashcards",
    # "followings",
    "followings.apps.FollowingsConfig",
    "steaks",
    "ads",
    "achievements",
    "subscriptions.apps.SubscriptionsConfig",
    "friends",

    "experts",
    "experts.experts_speaking",
    "experts.experts_writing",

    "candidates",
    "candidates.candidates_speaking",
    "candidates.candidates_writing",
]

AUTH_USER_MODEL = "accounts.User"

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'config.urls'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend"
    ],
}


SWAGGER_SETTINGS = {
    "DEFAULT_API_URL": "https://themeless-constance-zoomorphic.ngrok-free.dev",
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "AUTH_HEADER_TYPES": ("Bearer",),
}

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

WSGI_APPLICATION = 'config.wsgi.application'

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "ielts_db",
#         "USER": "postgres",
#         "PASSWORD": "postgres",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tashkent"
USE_I18N = True
USE_TZ = False

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "saidali20010209@gmail.com"
EMAIL_HOST_PASSWORD = "wxdq bncw zsot eocs"
DEFAULT_FROM_EMAIL = "saidali20010209@gmail.com"
