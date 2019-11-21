from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)
admin.site.register(models.Member)
admin.site.register(models.Active)
admin.site.register(models.Alumni)
