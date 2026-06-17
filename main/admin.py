# Register your models here.
from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display  = ('first_name', 'last_name', 'email', 'submitted_at')
    ordering      = ('-submitted_at',)
    search_fields = ('email', 'last_name')