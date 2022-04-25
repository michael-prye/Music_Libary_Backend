from ast import Return
import re
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song

@api_view(['GET','POST'])
def all_songs(request):
    if request.method == 'GET':
        query_set = Song.objects.all()
        serializer = SongSerializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer=SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET', 'PUT','DELETE'])
def single_song(request, pk):
    query_set = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer = SongSerializer(query_set)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer= SongSerializer(query_set, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        query_set.delete()
        return Response(status=status.HTTP_200_OK)
