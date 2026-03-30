from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # app
    path("api/core/", include("core.urls")),
    path("api/users/", include("users.urls")),
    # auth
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
]
