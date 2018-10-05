from django.urls import path
from . import views


app_name = 'banner'


urlpatterns = [
    path('<str:size>/<str:username>/', views.draw, name='draw'),
]
