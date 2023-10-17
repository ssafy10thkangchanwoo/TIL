from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 참조 : 내가 팔로우하는 사람들 ,  참조 자체의 정의: 한 모델에서 다른 모델을 가르킨다.
    # symmetrical 를 따로 False로 설정 안하면 자동맞팔이 됨
    # me.followings.all() 의 역참조는 me.user_set.all() 
    # 이름이 너무 직관적이지 않아 related_name = 'followers' 사용
    # 다시 말하지만 기존 유저 테이블에 변화는 없음. 
    followings = models.ManyToManyField('self', symmetrical = False, related_name = 'followers')
    # 여기서 'self'는 대댓글을 생각하라는데 . . . 
