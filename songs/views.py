from ast import Return
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song

@api_view(['GET'])
def all_songs(request):
    if request.method == 'GET':
        query_set = Song.objects.all()
        serializer = SongSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def single_song(request, pk):
    query_set = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer = SongSerializer(query_set)
        return Response(serializer.data, status=status.HTTP_200_OK)
