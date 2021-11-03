from django.contrib import admin
from django.urls import path, include

from video_audio import urls as va_urls
from api import urls as api_urls

urlpatterns = [
    path('', include(va_urls)),
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls))
]
