from django.shortcuts import render
from django.views.generic import View

from .scripts import check_exceptions


class VideoView(View):
    @staticmethod
    def get(request):
        return render(request, 'video_audio/base.html')

    @staticmethod
    def post(request):
        template = 'video_audio/base.html'
        url = request.POST.get('url')
        data = check_exceptions(url)

        if data.get('exception'):
            return render(request, template, context=data)

        return render(request, template, context={'data': [data]})
