from django.contrib import admin
from .models import Article


# admin.site.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created._at", "updated_at"]


admin.site.register(Article, ArticleAdmin)



