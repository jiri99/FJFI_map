"""fjfimap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import develop.views as allviews

urlpatterns = [
    path('', allviews.home_view, name='home'),
    path('admin/', admin.site.urls),
    path('homepage/', allviews.homepage_view, name='homepage'),
    path('display/', allviews.display_view, name='display'),
    path('classes/', allviews.classes_view, name='classes'),
    path('important/', allviews.important_view, name='important'),
    path('others/', allviews.others_view, name='others'),
    path('wc/', allviews.wc_view, name='wc'),
    path('navbar/', allviews.navbar_view, name='navbar'),
    path('room_search/', allviews.room_search_view, name='room_search'),
    path('search/', allviews.search_view, name='search'),
    path('favourite/', allviews.favourite_view, name='favourite'),
    path('room_detail/<room_id>', allviews.room_view, name='room_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)