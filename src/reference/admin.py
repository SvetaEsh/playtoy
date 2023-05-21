from django.contrib import admin
from . import models
admin.site.register(models.City)
admin.site.register(models.PublicHoliday)
admin.site.register(models.WorkDay)

# Register your models here.
