from django.db import models


class VideoInfo(models.Model):
    title = models.TextField()
    length = models.TextField()
    video_type = models.TextField()
    url = models.URLField()
    audio = models.URLField()
    audio_type = models.TextField()
