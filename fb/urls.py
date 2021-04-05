from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='fb-home'),
    path('about/', views.about, name='fb-about'),
]
