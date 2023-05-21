from django.contrib import admin
from . import models
admin.site.register(models.Category)
admin.site.register(models.Type)
admin.site.register(models.Product)
# Register your models here.
