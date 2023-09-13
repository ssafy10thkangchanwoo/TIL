from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def loginPage(request):
    return render(request, "myapp/loginPage.html")

def login(request):
    print(request.GET)
    context = {
        "id" : request.GET.get("id"),
        "password": request.GET.get('password')
    }

    return render(request, "myapp/loginResult.html", context)

def hello(request, name):
    print(f'name:{name}')
    context = {
        "name":name
    }
    return render(request, 'myapp/hello.html', context)

def hello2(request, age):
    print(f'name:{age}')
    context = {
        "name":age
    }
    return render(request, 'myapp/hello.html', context)