from django.shortcuts import render, redirect
from .models import ContactSubmission

# Create your views here.
def main(request):
    render(request,'main/index.html')


def contact(request):
    if request.method == 'POST':
        ContactSubmission.objects.create(
            first_name = request.POST.get('first_name', '').strip(),
            last_name  = request.POST.get('last_name', '').strip(),
            email      = request.POST.get('email', '').strip(),
        )
        return redirect('/?submitted=true')
    return redirect('/')