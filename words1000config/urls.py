from django.urls import path
from django.urls import include
from django.contrib import admin
from words.views import pageNotFound
from words1000config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('words.urls')),
]


handler404 = pageNotFound


# if settings.DEBUG:
    # urlpatterns += static(document_root=settings.MEDIA_ROOT)
