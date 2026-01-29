from .root_settings import *


INSTALLED_APPS += [
    "rest_framework",
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",  # Рендеринг JSON
        "rest_framework.renderers.BrowsableAPIRenderer",  # Рендеринг браузерного API
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",  # Аутентификация по токену
        "rest_framework.authentication.SessionAuthentication",  # Аутентификация по сессии
    ],
}
