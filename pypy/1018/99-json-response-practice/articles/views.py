from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.


# @api_view(['GET'])
@api_view()
def article_json(request):
    articles = Article.objects.all()
    # articles 의 데이터를 기존에는 context로 보냈는데 
    # 이제는 ArticleSerializer 거치고 
    serializer = ArticleSerializer(articles, many=True)
    
    return Response(serializer.data)
