from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home_"),
    path('index',views.index,name="index_")
]