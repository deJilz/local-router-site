from django.contrib import admin

# Register your models here.
from django.contrib import admin
from door_opener.models import timeStamp#Post, Category


class timeStampAdmin(admin.ModelAdmin):
    pass

admin.site.register(timeStamp, timeStampAdmin)
#admin.site.register(Category, CategoryAdmin)