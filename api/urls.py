from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('downloader', views.VideoViewSet)


urlpatterns = router.urls
