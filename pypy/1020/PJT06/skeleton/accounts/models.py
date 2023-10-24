from django.db import models
from django.contrib.auth.models import AbstractUser
# auth도 models을 가졌을꺼고
# contrib은 폴더인데... 왜 클래스처럼 접근하지?
# __init__.py 생성자, 클래스처럼 접근하게 해줌
# migrations, accounts..등등 앱파일들도 다 __init__ 가지고 있음
# Create your models here.
class User(AbstractUser):
    pass 