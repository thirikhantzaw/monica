from django.urls import path
from .views import HomePage
from .models import *

urlpatterns = [
    path('home/', HomePage)
]