from django.contrib import admin
from .models import (
                    URLs,
                    Redirects,
                    )
# Register your models here.


admin.site.register(URLs)
admin.site.register(Redirects)

