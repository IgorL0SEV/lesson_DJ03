from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_news_time'),
    path('create_news/', views.create_news, name='add_news')
]
