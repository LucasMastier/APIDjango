from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Item
from .serializers import ItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
