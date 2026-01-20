import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include('allauth.socialaccount.urls')),
    path("", include("core.urls")),
    path("", include("users.urls")),
    path("", include("settings.urls")),
    path("", include("game.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
