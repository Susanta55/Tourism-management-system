from . import views
from django.urls import path
from .views import *

urlpatterns = [
    path('login',views.login_user, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('verify/<str:id>/<str:token>/', views.verify, name='verify'),
    
]