from .root_settings import *


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'grachev613@gmail.com'          
EMAIL_HOST_PASSWORD = 'vgcfqpzgjrvefmyw'    
DEFAULT_FROM_EMAIL = 'grachev613@gmail.com'