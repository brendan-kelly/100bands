from django.contrib import admin
from .models import Concert


@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('band', 'date', 'want_level', 'user')
