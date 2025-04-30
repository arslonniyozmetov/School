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


from django.http import JsonResponse


def contactform(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        contact_info = request.POST.get('contact_info', '').strip()
        message = request.POST.get('message', '').strip()

        if not all([name, contact_info, message]):
            return JsonResponse({'success': False, 'error': 'Iltimos, barcha maydonlarni to\'ldiring'})

        # Telegramga yuborish
        telegram_message = (
            f"<b>Yangi xabar!</b>\n\n"
            f"<b>Ism:</b> {name}\n"
            f"<b>Aloqa:</b> {contact_info}\n"
            f"<b>Xabar:</b>\n{message}"
        )

        send_to_telegram(telegram_message)

        return JsonResponse({'success': True})
    return None


def teacher_view(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})


import requests
from django.conf import settings


def send_to_telegram(message):
    bot_token = settings.TELEGRAM_BOT_TOKEN
    for chat_id in settings.TELEGRAM_CHAT_IDS:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        try:
            response = requests.post(url, json={
                'chat_id': chat_id,
                'text': message,
                'parse_mode': 'HTML'
            })
            print(f"Chat ID {chat_id} ga yuborildi. Status: {response.status_code}")
        except Exception as e:
            print(f"Chat ID {chat_id} ga xabar yuborishda xatolik: {e}")




def news_list(request):
    news_items = News.objects.all().order_by('-date_posted')
    paginator = Paginator(news_items, 6)  # Sahifada 6 ta yangilik
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj})

def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    return render(request, 'news_detail.html', {'news': news_item})