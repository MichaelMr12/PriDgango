from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('cub/', cub, name='cub'),
    path('pri/<int:number_student>/', pri_id, name='spisok_pri'),
    path('pri/<slug:cat>/', categories, name='category'),


]
