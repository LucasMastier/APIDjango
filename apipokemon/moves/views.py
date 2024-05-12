from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Move
from .serializers import ItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_move(request, move_id):
    move = get_object_or_404(Move, pk=move_id)
    serializer = ItemSerializer(move)
    return Response(serializer.data)
