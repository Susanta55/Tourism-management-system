from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('pagenotfound',views.pagenotfound,name='pagenotfound'),
    path('about_us',views.about_us,name='about_us'),
    path('terms',views.terms,name='terms'),
    path('FAQ',views.FAQ,name='FAQ'),


    
]