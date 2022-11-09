from django.urls import path

from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from develop.views import home_view, homepage_view, display_view, list_view


app_name = 'frontend'

urlpatterns = [
    path('', views.index, name='index'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
