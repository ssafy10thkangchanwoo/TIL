from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm # 로그인 할 떄 활용
from .forms import CustomUserCreationFrom


@require_http_methods(['GET', 'POST'])
def signup(request):
    # 로그인 하는 유저가 사용하는 곳은 아니지?
    if request.user.is_atuenticated:
        return redirect('boards:index')
    
    # METHOD가 GET일 때와 POST 일 때
    # 실제로 회원가입 진행
    if request.method == "POST": # 생성
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            # 저장 및 자동 로그인
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    
    elif request.method == "GET": # 회원가입 화면 보여주기
        form = CustomUserCreationFrom()
    context = {
        'form': form, 
    } 
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

# 세션 삭제 -> POST 
@require_POST
def logout(request):
    # 로그인 된 사용자만 로그아웃
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("board:index")
