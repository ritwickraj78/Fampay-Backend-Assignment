from django.shortcuts import render

# Create your views here.get_videos_list,
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import YoutubeVideo
from api.serializers import YoutubeVideoSerializer


class VideoList(APIView):

    def get(self, request, format=None):
        videos = YoutubeVideo.objects.all()
        serializer = YoutubeVideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
