from django.shortcuts import render

# Create your views here.
def index(request):
    # 어떤 화면울 보여줄지 return함
    return render (request, "articles/index.html") # 이런 화면을 보여줄거야.