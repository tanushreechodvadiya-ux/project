from django.contrib import admin
from .models import *

# Register your models here.
class contactform(admin.ModelAdmin):
    list_display = ['cname','email','message','file_photo','submitted_at']

admin.site.register(ContactMessage,contactform)