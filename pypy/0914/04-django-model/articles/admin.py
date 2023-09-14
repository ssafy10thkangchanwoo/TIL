from django.contrib import admin
from .models import Article
# Register your models here.

# Article 모델 클래스를 admin site에 등록

# admin 사이트에 등록한다.
admin.site.register(Article)