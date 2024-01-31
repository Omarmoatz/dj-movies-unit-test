from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('',views.ShowViewSets)


app_name = 'movies'

urlpatterns = [
    path('viewSet/', include(router.urls)),
    
    path('list/', views.shows_list),
    path('detail/<int:pk>/', views.shows_detail),
]
