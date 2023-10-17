from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    # , related_name='like_article')
    # article에 새로운 테이블이 생겨난게 아니다. 중개테이블이 생긴것 뿐
    # user와 like_users의 역참조 이름이 같아 충돌 발생. 
    # related_name을 사용하여 이름 바꿔 충돌 제거 
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL
    , related_name='like_article') 
    # 중개테이블 like_user은 article에 생기진 않았다.
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
