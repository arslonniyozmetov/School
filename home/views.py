from django.core.paginator import Paginator
from .models import News  # Agar News modeli shu joyda bo‘lsa
from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'index.html')
def about_view(request):
    return render(request, 'about.html')
def contact_view(request):
    return render(request, 'contact.html')

def news_view(request):
    news_list = News.objects.all().order_by('-date')
    paginator = Paginator(news_list, 9)  # Har sahifada 9 ta xabar
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})

def gallery_view(request):
    return render(request, 'gallery.html')
def teacher_view(request):
    return render(request, 'teacher.html')
