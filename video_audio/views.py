from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from .scripts import check_exceptions
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
                return redirect(reverse("login"))

        return render(request, self.template_name)


class VideoView(TemplateView):
    template_name = 'video_audio/index.html'

    def post(self, request):
        url = request.POST.get('url')
        data = check_exceptions(url)
        user = request.user

        if data.get('exception'):
            return render(request, self.template_name, context=data)

        if user.id:
            data['user'] = user
            VideoInfo.objects.create(**data)

        return render(request, self.template_name, context={'data': [data]})


class UserVideoView(LoginRequiredMixin, ListView):
    template_name = 'video_audio/profile.html'

    def get_queryset(self):
        new_context = VideoInfo.objects.filter(user_id=self.request.user.id)

        return new_context
