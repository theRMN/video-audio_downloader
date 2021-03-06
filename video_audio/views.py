from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from .services import check_exceptions, check_user_id
from .models import VideoInfo


class RegisterView(TemplateView):
    template_name = 'registration/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                return redirect(reverse('login'))

        return render(request, self.template_name)


class VideoView(TemplateView):

    def get_template_names(self):
        if self.request.user.id:
            return 'video_audio/index_l.html'

        return 'video_audio/index.html'

    def post(self, request):
        url = request.POST.get('url')
        data = check_exceptions(url)
        user = request.user

        if data.get('exception'):
            return render(request, self.get_template_names(), context=data)

        check_user_id(data, user)

        return render(request, self.get_template_names(), context={'data': [data]})


class UserVideoView(LoginRequiredMixin, ListView):
    template_name = 'video_audio/history.html'

    def get_queryset(self):
        new_context = VideoInfo.objects.filter(user_id=self.request.user.id)

        return new_context

    def dispatch(self, request, *args, **kwargs):
        if request.user.id:
            return super().dispatch(request, *args, **kwargs)

        return redirect(reverse('main'))
