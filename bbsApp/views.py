from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import bbsModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def IndexView(request):
    return render(request, 'bbsApp/index.html')

def SignupView(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        
        try:
            User.objects.create_user(username_data, '', password_data)
            return redirect('login')

        except IntegrityError:
            return render(request, 'bbsApp/signup.html', {'error': 'このユーザーは既に登録されています。'})
    else:
        return render(request, "bbsApp/signup.html", {})
    
    #return render(request, "bbsApp/signup.html", {})

def LoginView(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            #userがいればこの処理が行われる
            return redirect('create')

        else:
            #userがいなければればこの処理が行われる
            #return redirect('login')
            return render(request, 'bbsApp/login.html', {'error': 'ユーザー名かパスワードが間違っています。'})
    return render(request, 'bbsApp/login.html')

def LogoutView(request):
    logout(request)
    return redirect('main')

#ListViewと同義
def MainView(request):
    object_list = bbsModel.objects.all()
    return render(request, 'bbsApp/main.html', {'object_list':object_list})

def DetailView(request, pk):
    object = bbsModel.objects.get(pk=pk)
    return render(request, 'bbsApp/detail.html', {'object':object})

class CreateClass(CreateView):
    template_name = 'bbsApp/create.html'
    model = bbsModel
    fields = ('university','title', 'content', 'user_name', 'evaluation')
    success_url = reverse_lazy('main')