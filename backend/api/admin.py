from django.contrib import admin
from .models import BaseURL, RedirectURL
# Register your models here.


admin.site.register(BaseURL)
admin.site.register(RedirectURL)
