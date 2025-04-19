from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import News,ContactMessage

# Create your views here.
def home_view(request):
    return render(request, 'index.html')
def about_view(request):
    return render(request, 'about.html')
def contact_view(request):
    return render(request, 'contact.html')

def gallery_view(request):
    return render(request, 'gallery.html')
def teacher_view(request):
    return render(request, 'teacher.html')



def news_list(request):
    news_items = News.objects.all().order_by('-date_posted')
    paginator = Paginator(news_items, 6)  # Sahifada 6 ta yangilik
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})

def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    return render(request, 'news_detail.html', {'news': news_item})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact_info = request.POST.get('contact_info')
        message = request.POST.get('message')
        if name and contact_info:
            ContactMessage.objects.create(name=name, contact_info=contact_info, message=message)
            return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')
