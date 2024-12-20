from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
<<<<<<< HEAD
	path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
=======
    path('login/', views.login_view, name='login'),
>>>>>>> 32ebcd5a2fd550772b2b0ed982a1c06e1cf50899
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('lost_items/', views.lost_items, name='lost_items'),
    path('post_item/', views.post_item, name='post_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('profile/', views.profile, name='profile'),
]