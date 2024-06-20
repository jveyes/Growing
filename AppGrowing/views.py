from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            response_data = {'message': 'Form submitted successfully!'}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})