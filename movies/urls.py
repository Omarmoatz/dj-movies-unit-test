from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('list/', views.shows_list),
    path('detail/<int:pk>/', views.shows_detail),
]
