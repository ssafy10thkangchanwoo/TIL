from django.urls import path
from articles import views


urlpatterns = [
    path('articles/', views.article_create_list),
    path('articles/<int:article_pk>/', views.article_create_list),
]
