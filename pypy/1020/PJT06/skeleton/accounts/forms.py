from django.contrib.auth.forms import UserCreationForm
# model 선택 세가지 방법 
# 1. 직접 가져오기 -> 권장 X 
from .models import User 
# 2. settings에 설정된 모델 가져오기 /문자열같이
# models.py에 작성할 때는 문자열로 적는 것이 좋다.
from django.conf import settings
# 3. get_user_model 메서드 활용
from django.contrib.auth import get_user_model


class CustomUserCreationFrom(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields