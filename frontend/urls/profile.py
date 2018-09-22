from django.urls import path
from .. import views

app_name = 'profile'

urlpatterns = [
    path('', views.profile, name='index'),
    path('logout/', views.logout_view, {'target': None}, name='logout'),
    path('register/', views.register, name='register')
]
