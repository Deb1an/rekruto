from django.urls import path
from . import views


urlpatterns = [
    path('', views.request_with_params)
]
