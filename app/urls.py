from django.urls import path
from .views import pen_detail, pen_create, pen_list

urlpatterns = [
     path('pen/create/', pen_create, name='pen_create'),
    path('pen/<str:unique_id>/', pen_detail, name='pen_detail'),
    path('', pen_list, name='pen_list'),  # Add this line for the home page
]
