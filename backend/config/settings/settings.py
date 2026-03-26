from .root_settings import *

INSTALLED_APPS += [
    # Lib
    "corsheaders",
    "rest_framework",
    "djoser",
    "rest_framework.authtoken",
    # App
    "core.apps.CoreConfig",
    "settings.apps.SettingsConfig",
    "users.apps.UsersConfig",
    "game.apps.GameConfig",
]

MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

AUTH_USER_MODEL = "users.User"

# DATABASES
if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": config("db_engine"),
            "NAME": config("db_name"),
            "USER": config("db_user"),
            "PASSWORD": config("db_password"),
            "HOST": config("db_host"),
            "PORT": config("db_port"),
            # Дополнительные настройки (опционально):
            "CONN_MAX_AGE": 600,  # время жизни соединения в секундах
            "OPTIONS": {
                "connect_timeout": 10,
            },
        }
    }

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATIC_URL = "/static/"

# Настройки Django REST Framework

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",     # Vite default
    "http://127.0.0.1:5173",
    "http://localhost:3000",     # если раньше был CRA
    "http://127.0.0.1:3000",
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
}
