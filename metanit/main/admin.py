from django.contrib import admin

# Register your models here.

from .models import reg
admin.site.register(reg);

from .models import info_modules
admin.site.register(info_modules);

from .models import SPP
admin.site.register(SPP);