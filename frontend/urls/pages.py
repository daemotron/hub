from django.urls import path
from .. import views


app_name = 'pages'


urlpatterns = [
    path('privacy/', views.PrivacyView.as_view(), name='privacy'),
    path('legal/', views.LegalView.as_view(), name='legal'),
]
