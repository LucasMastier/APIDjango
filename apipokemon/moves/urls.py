from django.urls import path
from .views import get_move

urlpatterns = [
    path('', get_move),
]
