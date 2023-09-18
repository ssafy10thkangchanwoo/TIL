from django.db import models

# Create your models here.

# Article이라는 데이터 타입을 만든다.
# 근데 장고의 기능을 쓸 거니까 장고의 모델클래스를 상속받는다.
# id는 django에서 자동생성
# 작성한 model 클래스는 최종적으로 DB에 테이블구조를 만듬.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
