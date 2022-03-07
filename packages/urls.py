from . import views
from django.urls import path



urlpatterns = [
    path('',views.packages, name='packages'),
    path('<int:id>',views.package_detail, name='package_detail'),

]
