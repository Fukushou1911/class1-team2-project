from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('post_item/', views.post_item, name='post_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('profile/', views.profile, name='profile'),
]