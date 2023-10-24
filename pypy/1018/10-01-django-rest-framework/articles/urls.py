from django.urls import path
from articles import views


urlpatterns = [
    path('articles/',views.article_list),
    path('articles/<int:article_pk>/', views.article_detail)
    # path('articles/create/') 
    # REST기법에서는 url을 식별하는데에만 쓰임
]
