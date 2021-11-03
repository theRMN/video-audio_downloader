from django.urls import path

from video_audio import views

urlpatterns = [
    path('', views.VideoView.as_view())
]

