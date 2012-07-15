#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Admin configurations for the blog engine app."""

from blogengine.models import Article, Category
from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    """Model admin for the articles."""
    fieldsets = [
        ('Your article', {'fields': ['title', 'text']}),
        ('Metadata', {'fields': ['author', 'creation_time', 'category']}),
        ]
    list_display = ('title', 'creation_time', 'author', 'category')
    list_filter = ['category', 'author']
    search_fields = ['title', 'author']
    date_hierarchy = 'creation_time'


class ArticleInline(admin.StackedInline):
    """Allows to show article lists inline when editing categories."""
    model = Article
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    """Model admon for the categories."""
    fieldsets = [
        ('Category information', {'fields': ['name', 'description']}),
        ]
    inlines = [ArticleInline]
    list_display = ('name', 'description')
    search_fields = ['name']


# Register the desired models to be administered.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
