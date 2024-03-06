from django.contrib import admin
from .models import movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','Actor_1','Actor_2','Song_1','Song_2','director','producer')

# Register your models here.
admin.site.register(movie,MovieAdmin)
