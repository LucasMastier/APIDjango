from django.urls import path
from .views import get_item

urlpatterns = [
    path('', get_item),
]
