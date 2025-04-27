from django.core.paginator import Paginator
from.models import *
from django.shortcuts import render, get_object_or_404
from .models import Teacher

# Create your views here.
def home_view(request):
    return render(request, 'index.html')
def about_view(request):
    return render(request, 'about.html')
def contact_view(request):
    return render(request, 'contact.html')


def teacher_view(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})




def news_list(request):
    news_items = News.objects.all().order_by('-date_posted')
    paginator = Paginator(news_items, 6)  # Sahifada 6 ta yangilik
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})

def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    return render(request, 'news_detail.html', {'news': news_item})