from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('login', views.login_app),
    path('logout', views.logout_app),
]
