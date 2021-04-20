from django.db.models import Q
from django.shortcuts import render

# Create your views here.get_videos_list,
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import YoutubeVideo
from api.serializers import YoutubeVideoSerializer
from api.utils import get_videos_from_api


class VideoList(APIView):
    """
    API Class for getting all videos in the Database
    """
    def get(self, request, format=None):
        response = get_videos_from_api()
        videos = YoutubeVideo.objects.order_by('-published_date').all()
        paginator = PageNumberPagination()
        paginator.page_size = 20
        paginator.max_page_size = 20
        paginator.paginate_queryset(videos, request)
        serializer = YoutubeVideoSerializer(videos, many=True)
        return paginator.get_paginated_response(serializer.data)


class VideoSearch(APIView):
    """
    API to Search Videos from Database based on query term
    Request Parameter: q - Query String
    """
    def get(self, request, format=None):
        query = request.query_params.get('q')
        if query:
            videos = YoutubeVideo.objects.filter(Q(description__icontains=query) | Q(title__icontains=query)).all()
            paginator = PageNumberPagination()
            paginator.page_size = 20
            paginator.max_page_size = 20
            paginator.paginate_queryset(videos, request)
            serializer = YoutubeVideoSerializer(videos, many=True)
            return paginator.get_paginated_response(serializer.data)
