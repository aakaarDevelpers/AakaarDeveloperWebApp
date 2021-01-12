from django.shortcuts import render

def payment_index(request):
    context = {}
    return render(request, 'payments/Payment_site.html', context)