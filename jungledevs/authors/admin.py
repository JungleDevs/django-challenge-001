from django.contrib import admin
from django.contrib.admin import ModelAdmin

from jungledevs.authors.models import Author


@admin.register(Author)
class ArticleAdmin(ModelAdmin):
    list_display = ["name", "picture"]
    search_fields = ["name"]
    list_filter = ("name", )
