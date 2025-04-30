from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('teacher/', teacher_view, name='teacher'),
    path('contact/', contact_view, name='contact'),
    path('news/', news_list, name='news'),
    path('news/<slug:slug>/', news_detail, name='news_detail'),
    path('contactform/',contactform, name='contactform'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
