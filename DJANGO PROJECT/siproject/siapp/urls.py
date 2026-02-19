from django.urls import path
from . import views

urlpatterns = [
    path('', views.simpleinterest, name="si"),
]
