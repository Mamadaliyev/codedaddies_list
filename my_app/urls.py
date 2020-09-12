from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_search, name='home'),
    path('new_search', views.new_search, name='new_search')
]

