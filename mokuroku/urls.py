from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path(settings.DJANGO_ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("lists/", include("lists.urls")),
    path("", include("pages.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
