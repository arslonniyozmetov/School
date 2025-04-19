from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'index.html')
def about_view(request):
    return render(request, 'about.html')
def contact_view(request):
    return render(request, 'contact.html')
def news_view(request):
    return render(request, 'news.html')
def gallery_view(request):
    return render(request, 'gallery.html')
def teacher_view(request):
    return render(request, 'teacher.html')
