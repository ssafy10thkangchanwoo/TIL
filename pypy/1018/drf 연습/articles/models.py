from django.db import models

# Create your models here.
# 파이썬만이 알 수 있는 코드
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now = True)