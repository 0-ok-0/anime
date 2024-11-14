from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('topAnime/', views.topAnime, name='topAnime')
]