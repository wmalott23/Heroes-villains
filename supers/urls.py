from django.urls import path
from . import views


urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.supers_detail),
    path('<int:pk>/<int:id>/', views.supers_power),
    path('<str:super_name1>/<str:super_name2>/', views.supers_battle)
]