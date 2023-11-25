from django.contrib import admin
from .models import bookTable, ContactUS, SubEmail

# Register your models here.
admin.site.register(bookTable)
admin.site.register(ContactUS)
admin.site.register(SubEmail)