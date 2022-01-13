from django.conf import settings
from django.db import models


class VideoInfo(models.Model):
    title = models.TextField()
    length = models.TextField()
    resolution = models.TextField()
    video_url = models.URLField(max_length=1000)
    audio_url = models.URLField(max_length=1000)
    abr = models.TextField()
    image = models.URLField(max_length=1000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
