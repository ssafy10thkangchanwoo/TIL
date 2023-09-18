from django.urls import path

from . import views

app_name = "myapp"
urlpatterns = [
    path('index/', views.index, name='index'),
    path('myapp/', views.index),
    path('loginPage/', views.loginPage, name ="loginPage"),
    path('login/', views.login, name = "login"),
    path("hello/<str:name>/", views.hello),
    path("hello/<int:age>/", views.hello2)
]
