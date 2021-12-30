from django.urls import path, reverse_lazy
from django.contrib.auth import views

from video_audio import views as va

urlpatterns = [
    path('', va.VideoTemplateView.as_view(), name='main'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page=reverse_lazy('main')), name='logout'),
    path('register/', va.RegisterView.as_view(), name="register"),

]

