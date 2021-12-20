from django.db import models


class VideoInfo(models.Model):
    title = models.TextField()
    length = models.TextField()
    resolution = models.TextField()
    video_url = models.URLField()
    audio_url = models.URLField()
    abr = models.TextField()
