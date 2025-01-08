from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def post_item(request):
    if request.mthod == 'POST':
        new=item = LostItem(
            posted_by = request.user,)
        nes_item = save()
        return redirect('success-page-url')