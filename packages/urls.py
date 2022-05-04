from tokenize import Name
from unicodedata import name
from . import views
from django.urls import path



urlpatterns = [
    path('',views.packages, name='packages'),
    path('search',views.search, name='search'),
    path('success/<int:id>', views.success,name='success'),
    path('booking/checkout/<int:id>',views.checkout,name='checkout'),
    path('<str:slug>',views.package_detail, name='package_detail'),
    path('booking/<str:slug>',views.booking, name='booking'),
   

    
    


]
