from django.urls import path
from django.views.generic.base import RedirectView
from . import views


app_name = 'pages'


urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('home/', views.IndexView.as_view(), name='index'),
]
