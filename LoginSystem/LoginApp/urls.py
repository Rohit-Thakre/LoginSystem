from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLogin, name='login'),
    path('register/', views.Register, name='register'),
]
