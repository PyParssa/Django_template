from django.shortcuts import render

# Create your views here.
def main(request):
    render(request,'main/index.html')