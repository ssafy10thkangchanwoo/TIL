from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required
def delete(request):
    request.user.delete()
    return redirect('articles:index')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)

def profile(request, username):
    # User의 detail 페이지 
    # user 를 조회
    # 이때까지는 pk로 했었지.
    # person = 클래스.objects.get(username=username)
    # get_user_model은 현재 프로젝트에 등록되어 있는 계정에 관한 정보
    # accounts.models.User라고 봐도 됨
    User = get_user_model()
    person = User.objects.get(username=username)
    # person = get_user_model().objects.get(username=username) 
    # 이렇게 작성해도 무방
    context = {
        'person' : person,
    }
    return render(request, 'accounts/profile.html', context)

# 수정 전
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user: # 대상자가 내가 아니라면
        # if request.user in person.followers.all():
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user) 
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)

# def follow(request, user_pk):
#     you = get_user_model().objects.get(pk=user_pk)
#     me = request.user 
#     if me != you:
#             # 내가 상대방의 팔로우 목록에 있다면
#         if me in you.followers.all():
#             # 팔로우 취소
#             you.followers.remove(me)
#             # me.followings.remove(you) # 같음
#         else:
#             you.followers.add(me)
#             # me.followings.add(you)
#     return redirect('accounts:profile',you.username )
        
    # 팔로우하는 대상을 조회
    # 팔로우 취소/진행에 대한 기준
    # 팔로우 버튼 토글 
