from django.contrib import admin
from . import models

# Register your models here.

class HoodwatchMember(admin.TabularInline):
    model = models.HoodwatchMember


admin.site.register(models.Hoodwatch)
