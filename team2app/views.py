from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def index(request):
	return render(request, 'team2app/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # ログイン成功後にリダイレクト
        else:
            return render(request, 'team2app/login.html', {'error': 'ユーザー名またはパスワードが間違っています。'})
    return render(request, 'team2app/login.html')