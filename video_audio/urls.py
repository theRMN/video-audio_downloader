from django.urls import path

from video_audio import views

urlpatterns = [
    path('', views.VideoTemplateView.as_view())
]

