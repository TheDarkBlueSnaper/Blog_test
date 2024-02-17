from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'owner', 'category')
    list_filter = ('date', 'category')
    search_fields = ('title', 'owner__username', 'category__name')
    date_hierarchy = 'date'
    ordering = ('-date',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)