from rest_framework import serializers
from video_audio.scripts import youtube_downloader

from video_audio.models import VideoInfo


class VideoInfoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(read_only=True)
    length = serializers.CharField(read_only=True)
    video_type = serializers.CharField(read_only=True)
    audio_type = serializers.CharField(read_only=True)
    audio = serializers.URLField(read_only=True)

    class Meta:
        model = VideoInfo
        fields = '__all__'

    def create(self, validated_data):
        url = super().create(youtube_downloader(validated_data['url']))

        return url
