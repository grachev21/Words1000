from .root_settings import *


INSTALLED_APPS += [
    # App
    "core.apps.CoreConfig",
    "settings.apps.SettingsConfig",
    "users.apps.UsersConfig",
    "game.apps.GameConfig",
    # Libs
    "debug_toolbar",
    "django_browser_reload",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

# for debug_toolbar
INTERNAL_IPS = ["127.0.0.1"]
AUTH_USER_MODEL = "users.User"

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
            "ENGINE": config("DB_ENGINE"),
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": config("DB_HOST"),
            "PORT": config("DB_PORT"),
            # Дополнительные настройки (опционально):
            "CONN_MAX_AGE": 600,  # время жизни соединения в секундах
            "OPTIONS": {
                "connect_timeout": 10,
            },
        }
    }


STATICFILES_DIRS = [
    BASE_DIR / "static",  # Путь к общей статике
]

STATIC_ROOT = BASE_DIR / "staticfiles"  # Куда collectstatic соберёт файлы
STATIC_URL = "/static/"  # URL для статики

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
