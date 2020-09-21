from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_home,name='main_home'),
    path('profile',views.profile,name='profile')
]
