from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^category/([0-9]+)$', views.category),
    url(r'^author/([0-9]+)$', views.author),
    url(r'^video_storage$', views.video_storage),
    url(r'^streaming$', views.streaming),
    url(r'^stream_creation$', views.stream_creation),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

