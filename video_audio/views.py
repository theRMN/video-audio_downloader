from django.shortcuts import render
from django.views.generic import View

from .scripts import youtube_downloader


class VideoView(View):
    def get(self, request):
        return render(request, 'video_audio/base.html')

    def post(self, request):
        template = 'video_audio/base.html'
        data = youtube_downloader(request.POST.get('url'))
        return render(request, template, context={'data': [data]})
