from django.contrib import admin
from django.urls import path, include

from video_audio import urls as va_urls

urlpatterns = [
    path('', include(va_urls)),
    path('admin/', admin.site.urls),
]
