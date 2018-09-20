from django.urls import path
from .. import views

app_name = 'profile'

urlpatterns = [
    path('logout/', views.logout_view, {'target': None}, name='logout')
]
