
from django.urls import path
from .import views


app_name="accounts"
urlpatterns = [
    # 회원가입, 로그인, 로그아웃
    # url, views, form
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
