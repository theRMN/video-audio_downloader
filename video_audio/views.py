from django.shortcuts import render
from django.views.generic import TemplateView

from .scripts import check_exceptions


class VideoTemplateView(TemplateView):
    template_name = 'video_audio/base.html'

    def post(self, request):
        url = request.POST.get('url')
        data = check_exceptions(url)

        if data.get('exception'):
            return render(request, self.template_name, context=data)

        return render(request, self.template_name, context={'data': [data]})
