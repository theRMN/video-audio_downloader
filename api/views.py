from rest_framework.viewsets import ModelViewSet

from . import serializers
from video_audio.models import VideoInfo


class VideoViewSet(ModelViewSet):
    queryset = VideoInfo.objects.all()
    serializer_class = serializers.VideoInfoSerializer
