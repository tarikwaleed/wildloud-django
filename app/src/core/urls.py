from django.conf import settings
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home-view"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
