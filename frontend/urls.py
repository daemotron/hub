from django.urls import path
from django.views.generic.base import RedirectView
from . import views


app_name = 'pages'


urlpatterns = [
    path('', RedirectView.as_view(url='home/')),
    path('home/', views.IndexView.as_view(), name='index'),
    path('contact/', views.contact, name='contact'),
    path('contact/sent/', views.SentView.as_view(), name='sent'),
    path('privacy/', views.PrivacyView.as_view(), name='privacy'),
    path('legal/', views.LegalView.as_view(), name='legal'),
]
