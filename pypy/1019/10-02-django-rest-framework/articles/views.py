from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample
from drf_spectacular.types import OpenApiTypes

@extend_schema(
        examples=[
            OpenApiExample('Article', value={'title':'title', 'content':'content'}, status_codes=[201]),
            OpenApiExample('Error', value={'field':'err msg'}, status_codes=[201]),
            ],
        responses={
            (201, 'application/json') : OpenApiTypes.OBJECT,
            (400, 'application/json') : OpenApiTypes.OBJECT,
        },      
        request={'application/json' : OpenApiTypes.OBJECT},
        # application/json요청이 오면 OpenApiTypes.OBJECT로 간다.
)
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        
        # articles = Article.objects.all()
        # 빈 쿼리셋이면 404를 반환한다.
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    # try:
    #     article = Article.objects.get(pk=article_pk)
    # except:
    #     htt... 이걸 아래 한줄로 처리할 수 있다.
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        # serializer는 기본적으로 모든 데이터를 요구
        # 일부 field만 수정할 수 있게 하려면 particla=True 를 기입
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) # Comment 전체 데이터 조회
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many = True)
    return Response(serializer.data)

@api_view(['GET','DELETE','PUT']) # Comment 단일 데이터 조회
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT) 

    elif request.method == 'PUT':
        # 댓글은 한가지 데이터밖에 없으니 딱히 partial 이 필요하지 않음
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save() # 왜 article이 안들어가도 됐다고..?
            # 코멘트 자체만 수정한거니 딱히 article 안들어가도 될 듯
            # article은 이미 Foreignkey로 연결되어 있으니
            return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    # get_object_or_404 정확한 에러현황을 받을 수 있음
    # 내가 잘못했는지 서버가 잘못했는지 확인 가능, 
    article = get_object_or_404(Article, pk=article.pk)
    serializer = CommentSerializer(data=request.data)
    # 조회는 가능하게, 유효성검사는 제외할 수 있게 끔 -> 읽기 전용 필드
    if serializer.is_valid(raise_exception=True):
        # serializer의 article값에 article
        serializer.save(article=article) 
        # CommentSerializer에서 외래키는 받았었나..?
        # 외래키는 있으니까 is_valid에서는 검사하지 않게 해. 나중에 넣을게
        # CommentSerializer 에서 article field는 read_only_field로 지정한다

        return Response(serializer.data, status = status.HTTP_201_CREATED)
#    raise_exception=Ture가 기입되면 유효성 검사시 실패하면 에러값 반환 


def index(request):
    articles = get_list_or_404(Article)
    # 게시물 없을 때 에러가 나오는 문제가 있음.
    # API를 개발할 때 유용한 기능