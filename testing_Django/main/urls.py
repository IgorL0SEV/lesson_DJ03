from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news', views.news, name='page2'),
    path("data", views.data, name='data'),
    path("test", views.test, name='test')

]
