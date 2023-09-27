from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk): # 배리어블라우팅, 이름 매칭 되야 함.
    article = Article.objects.get(pk=pk) # 딱 하나만 있을 때 에러가 안난다.
    # 왼쪽의 pk는 검색할 때 table의 컬럼을 말하고 오른쪽의 pk는 배리어블라우팅에서 온 것  
    # 겟은 쿼리셋을 리턴하지 않음.

    context = {
        'article' : article,
    }
    return render(request, 'article/detainl.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):

    # 1 
    # article = Article()
    # article.title = request.GET.get('title')
    # article.title = request.GET.get('content')
    # article.save()

    # 2 
    article = Article(title=title, content=content) 
    article.save()

    # 3 
    # Article.object.create(title=title, content =content)

    return render(request, 'articles/create.html')
