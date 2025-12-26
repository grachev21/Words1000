from .root_settings import *

INSTALLED_APPS += [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.vk",
]

SITE_ID = 2

MIDDLEWARE += [
    "allauth.account.middleware.AccountMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SOCIALACCOUNT_PROVIDERS = {
    "vk": {
        "APP": {"client_id": config("vk_id"), "secret": config("vk_secret"), "key": config("vk_key")}
    },
}

SOCIALACCOUNT_PROVIDERS = {
    'vk': {
        'APPS': [  # Ключ ВО МНОЖЕСТВЕННОМ ЧИСЛЕ - 'APPS', не 'APP'!
            {
                'client_id': config("vk_id"),  # ID приложения VK
                'secret': config("vk_secret"),  # Защищенный ключ
                'key': config("vk_key"),  # Сервисный ключ
            }
        ],
        'SCOPE': ['email', 'photos'],  # Права доступа
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'METHOD': 'oauth2',
        'VERSION': '5.131',
    }
}