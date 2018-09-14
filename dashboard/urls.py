from django.urls import path
from . import views


app_name = 'dashboard'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('settings/', views.settings, name='settings'),
]
