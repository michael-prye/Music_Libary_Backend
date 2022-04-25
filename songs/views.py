from ast import Return
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

@api_view([])
def all_songs(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)

@api_view([])
def single_song(request, pk):
    if request.method == 'get':
        return Response(status=status.HTTP_200_OK)
