from django.conf import settings
from django.urls import path
from.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('teacher/', teacher_view, name='teacher'),
    path('news/', news_list, name='news'),
    path('news/<slug:slug>/', news_detail, name='news_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
