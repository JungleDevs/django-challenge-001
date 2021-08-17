from django.contrib import admin
from django.contrib.admin import ModelAdmin

from jungledevs.articles.models import Article, Category


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ["author", "category", "title", "summary", "firstParagraph", "body"]
    search_fields = ["author", "category", "title"]
    list_filter = ("author", "title", "category")


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ("name", )
