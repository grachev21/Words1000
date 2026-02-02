from .root_settings import *

INSTALLED_APPS += [
    # App
    "core.apps.CoreConfig",
    "settings.apps.SettingsConfig",
    "users.apps.UsersConfig",
    "game.apps.GameConfig",
    # Libs
    "django_cotton",
    "debug_toolbar",
    "django_browser_reload",
    "heroicons",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

# TEMPLATES
TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates", BASE_DIR / "icons"]
TEMPLATES[0]["OPTIONS"]["context_processors"] += [
    "core.context_processors.site_settings",
    "config.context_processors.global_context",
]
TEMPLATES[0]["OPTIONS"]["builtins"] = [
    "heroicons.templatetags.heroicons",
]

# for debug_toolbar
INTERNAL_IPS = ["127.0.0.1"]
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


STATICFILES_DIRS = [
    BASE_DIR / "static",  # Путь к общей статике
]

STATIC_ROOT = BASE_DIR / "staticfiles"  # Куда collectstatic соберёт файлы
STATIC_URL = "/static/"  # URL для статики

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
