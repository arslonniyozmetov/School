from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('admin/messages/', views.message_list, name='message_list'),
    path('admin/messages/<int:pk>/read/', views.mark_as_read, name='mark_as_read'),
]