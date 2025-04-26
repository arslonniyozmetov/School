from django.urls import path
from .views import *
from .views import news_list, news_detail


urlpatterns = (
    path('', home_view, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('teacher/',teacher_view, name='teacher'),
path('news/', news_list, name='news'),
    path('news/<slug:slug>/', news_detail, name='news_detail'),
)