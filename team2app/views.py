from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment


def index(request):
	return render(request, 'team2app/index.html')

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
