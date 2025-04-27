import requests
from django.shortcuts import render

from .models import ContactMessage

# Telegram Bot Token va Chat ID
TELEGRAM_BOT_TOKEN = '7202357879:AAHtxkIueQ-qNT4TNaeF19PNuDwD7FA11RM'
TELEGRAM_CHAT_ID = ['7582735874,7947056719']


def contact_view(request):
    success = False

    if request.method == 'POST':
        name = request.POST.get('name')
        contact_info = request.POST.get('contact_info')
        message = request.POST.get('message')

        if name and contact_info and message:
            # 1. Ma'lumotni bazaga saqlaymiz
            ContactMessage.objects.create(name=name, contact_info=contact_info, message=message)

            # 2. Telegramga yuboramiz
            text = f"""🆕 *Yangi Aloqa Xabari* 📩
            👤 *Ism:* {name}
            📞 *Kontakt:* {contact_info}
            📝 *Xabar:*
            _{message}_"""

            # Ikki chat_id ga yuborish
            chat_ids = [7582735874, 7947056719]

            for chat_id in chat_ids:
                url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'Markdown'}
                requests.post(url, data=payload)

            success = True

    return render(request, 'contact.html', {'success': success})
