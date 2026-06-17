from django.urls import path
from .views import main,contact

urlpatterns = [
    path("",main),
    path('contact/', contact, name='contact'),
]