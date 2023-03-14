from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_filter = ['timestamp',]
    list_display = ['id', 'title', 'timestamp']
    list_display_links = ['id', 'title']
