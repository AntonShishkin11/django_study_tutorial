from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), #homepage
    path('show_smth/', views.show_smth, name="smth")
]