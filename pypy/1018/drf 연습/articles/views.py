from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
# 데이터20개 생성 : python manage.py seed articles --number=20 
from rest_framework import status

from . models import Article 
from .serializers import ArticleSerializer, ArticleListSerializer

@api_view(["GET", "POST"])
def article_list(request):
    # GET-> 모든 article 조회
    if request.method == 'GET':
        articles = Article.objects.all()
        # 어떤 형식을 json 형식의 데이터로 바꾸겠습니까?
        serializer = ArticleListSerializer(articles, many=True)
        # 여러개를 직렬화 하려면 many=True 
        return Response(serializer.data)
    # POST 요청은 모든 Article을 생성하는 요청 
    elif request.method == "POST":
        # 파이썬에서 온 데이터가 아닌 무언가의 데이터를 씀
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
