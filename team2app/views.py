<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment

=======
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
>>>>>>> 32ebcd5a2fd550772b2b0ed982a1c06e1cf50899

def index(request):
	return render(request, 'team2app/index.html')

<<<<<<< HEAD
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'team2app/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # コメントを作成する処理
        text = request.POST.get('text')
        if text:
            Comment.objects.create(post=post, text=text)
            return redirect('post_detail', post_id=post_id)
    return render(request, 'team2app/post_detail.html', {'post': post})
=======
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
>>>>>>> 32ebcd5a2fd550772b2b0ed982a1c06e1cf50899
