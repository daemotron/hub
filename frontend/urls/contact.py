from django.urls import path
from .. import views


app_name = 'contact'


urlpatterns = [
    path('', views.contact, name='index'),
    path('sent/', views.SentView.as_view(), name='sent'),
]