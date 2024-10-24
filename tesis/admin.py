from django.contrib import admin
from .models import Thesis

@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'advisor', 'year', 'category', 'visible')
    search_fields = ('title', 'author', 'advisor', 'category')
    list_filter = ('visible', 'category', 'year')