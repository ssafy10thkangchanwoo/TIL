from django.urls import path
from articles import views

# 500은 서버측 에러 ? 클라이언트 잘못
# 서버가 중단된 것

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    # 전에는 comments/create라고 표현했었는데 REST관점에서 좋지 않음
    # POST로 표기하니까 작성이라고 알아 먹음
    path('articles/<int:article_pk>/comments/', views.comment_create)
    

]
