from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_token),
    path('get/',views.get_token),
    path('authenticate/',views.authenticate_token),
]
