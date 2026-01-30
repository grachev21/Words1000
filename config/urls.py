from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),

    # Маршруты dj-rest-auth — включая регистрацию и соцвход
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    # Если используешь allauth для соцаккаунтов
    path('accounts/', include('allauth.urls')),

    path("", include("core.urls")),
    path("", include("users.urls")),
    path("", include("settings.urls")),
    path("", include("game.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
