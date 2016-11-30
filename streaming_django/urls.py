from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from core import views as core_views
from streams import views as streams_views
from videos import views as videos_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.index),
    url(r'^test_raw$', streams_views.test_raw),
    url(r'^test_server$', streams_views.test_server),
    url(r'^test$', streams_views.test),
    url(r'^article/([0-9]+)$', core_views.article),
    url(r'^category/([0-9]+)/([a-zA-Z0-9_?\(\)\']+)$', videos_views.category),
#url(r'^category/([0-9]+)$', videos_views.category),
    url(r'^author/([0-9]+)$', videos_views.author),
    url(r'^video_storage$', videos_views.video_storage),
    url(r'^streaming$', streams_views.streaming),
    url(r'^stream_creation$', streams_views.stream_creation),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

