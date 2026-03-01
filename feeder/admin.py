from django.contrib import admin
from .models import FeedingTime

# Register your models here.
admin.site.register(FeedingTime)

'''
@admin.register(FeedingTime)
class FeedingAdmin(admin.ModelAdmin):
    list_display = ('time')
'''