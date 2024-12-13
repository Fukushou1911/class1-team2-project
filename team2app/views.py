from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import LostItem

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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 登録成功後にログインページへリダイレクト
    else:
        form = UserCreationForm()
    return render(request, 'team2app/register.html', {'form': form})

def lost_items(request):
    query = request.GET.get('query')  # GETパラメータから検索語を取得
    if query:
        items = LostItem.objects.filter(
            title__icontains=query
        ) | LostItem.objects.filter(
            description__icontains=query
        )
    else:
        items = LostItem.objects.all()
    return render(request, 'team2app/lost_items.html', {'items': items, 'query': query})


def post_item(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        date_lost = request.POST['date_lost']
        image = request.FILES.get('image')
        LostItem.objects.create(
            title=title,
            description=description,
            location=location,
            date_lost=date_lost,
            image=image,
            posted_by=request.user
        )
        return redirect('lost_items')
    return render(request, 'team2app/post_item.html')

@csrf_exempt
@login_required
def delete_item(request, item_id):
    item = get_object_or_404(LostItem, id=item_id)
    posted_by = item.posted_by  # 投稿者を取得

    if request.method == "POST":
        if item.posted_by == request.user:  # 投稿者のみが削除可能
            item.delete()  # 誰でも削除可能
            # 投稿者にありがとうポイントを付与
            posted_by.thank_you_points += 1
            posted_by.save()
            messages.success(request, f"投稿が削除されました。投稿者にありがとうポイントが1ポイント付与されました！")

        else:
            messages.error(request, "この投稿を削除する権限がありません。")
    return redirect('lost_items')

def profile(request):
    return render(request, 'team2app/profile.html')

