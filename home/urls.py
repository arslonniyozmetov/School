from django.conf import settings
from django.urls import path, include
from .views import home_view, about_view, teacher_view, news_list, news_detail
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('teacher/', teacher_view, name='teacher'),
    path('news/', news_list, name='news'),
    path('news/<slug:slug>/', news_detail, name='news_detail'),
    path('contact/', include('contactmessages.urls')),  # <-- bu yerda contact_view o‘rniga include
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
