from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactMessage
from django.contrib.auth.decorators import login_required

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contacts/success.html')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact.html', {'form': form})

@login_required
def message_list(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'contacts/admin/list.html', {'messages': messages})

@login_required
def mark_as_read(request, pk):
    message = ContactMessage.objects.get(pk=pk)
    message.is_read = True
    message.save()
    return redirect('message_list')