LOGIN_URL = '/accounts/login/'

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def post_item(request):
    if request.method == 'POST':
        pass
    else:
        messages.info(request, '投稿するにはログインが必要です。')