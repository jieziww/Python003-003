from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Shawshank
from .form import LoginForm

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        search_dict = dict()
        query = request.GET.get('q', '')
        if query:
            search_dict['content__contains'] = query
        else:
            search_dict['rating__gt'] = 3
        comments = Shawshank.objects.filter(**search_dict)
        return render(request, 'index.html', locals())
    else:
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})



def login_app(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect("/index")
            else:
                return HttpResponse('登录失败')

    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})


def logout_app(request):
    logout(request)
    return HttpResponse('成功退出登录！')

