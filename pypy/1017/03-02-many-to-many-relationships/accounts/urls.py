from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    # 프로필은 게시판보다 유저쪽에 가깝다 판단하여 accounts에 추가
    # profile/ 이 없으면 문제가 생길 수 있다는데 왜..?
    # url에 요청이 오면 <username> 이게 문자열로 들어온 모든 것을 username으로 인식하여 항상 username에 걸릴 수 있다
    path('profile/<username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name = 'follow')
]
