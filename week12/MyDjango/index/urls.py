from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:phoneid>/<str:title>/', views.comments, name='comments')
]
