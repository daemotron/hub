"""hub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', include('frontend.urls.index')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('banner/', include('banner.urls')),
    path('captcha/', include('captcha.urls')),
    path('contact/', include('frontend.urls.contact')),
    path('dashboard/', include('dashboard.urls')),
    path('markdownx/', include('markdownx.urls')),
    path('pages/', include('frontend.urls.pages')),
    path('profile/', include('frontend.urls.profile')),
]
