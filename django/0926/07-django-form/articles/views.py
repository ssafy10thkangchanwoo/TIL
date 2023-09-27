from django.shortcuts import render, redirect, get_object_or_404 # 있으면 가져오고 없으면 404 에러를 발생시키겠다.
from django.views.decorators.http import require_POST  

from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article,  pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)


def create(request):
    # 요청의 메서드가 POST -> create, GET -> new
    if request.method == 'POST':
        
    
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            #유효성검사가 통과된 경우
            article = form.save() # save에 return에 있으니 바로 article 사용
            return redirect('articles:detail',article.pk)


    # 요청의 메서드가 POST가 아니라면 # POST, GET 외의 메서드가 더 있다.
    else: 
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # article = Article(title=title, content=content)
    # article.save()
    # return redirect('articles:index')

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     # 기존 내용이 나오게 하려면  instance인자에 article을 
    
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk) # 공통

    if request.method == 'POST':
        # article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article) # 이렇ㄱㅔ 데이터를 보내왔다. 어떻게 바꿀껀데?
        if form.is_valid:# 유효한 데이터로만 이루어졌는지?
            form.save() # 
            return redirect('articles:detail', article.pk)
        # context = {
        #     'form' : form, 
        # } # 실패할 때 실패한 이유 렌더링할꺼
        # return render(request, 'articles/edit.html', context)
        # # article.title = request.POST.get('title')
        # # article.content = request.POST.get('content')
        # # article.save()
        # return redirect('articles:detail', article.pk)
    else:
        # article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)
        # 기존 내용이 나오게 하려면  instance인자에 article을 
        
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)
