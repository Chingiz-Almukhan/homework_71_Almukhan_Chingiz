from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('accounts.urls')),
    path("insta/", include('posts.urls')),
    path("api/", include('api.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)