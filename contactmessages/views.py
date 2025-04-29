# views.py
import requests
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm


def send_to_telegram(message):
    bot_token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    try:
        response = requests.post(url, json={
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'HTML'
        })
        return response.status_code == 200
    except Exception as e:
        print(f"Telegramga xabar yuborishda xato: {e}")
        return False


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Telegramga xabar tayyorlash
            message = (
                f"<b>Yangi Xabar!</b>\n\n"
                f"<b>Ism:</b> {contact.name}\n"
                f"<b>Yuboruvchi::</b> {contact.contact_info}\n"
                f"<b>Xabar:</b>\n{contact.message}"
            )

            # Telegramga yuborish
            send_to_telegram(message)

            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})