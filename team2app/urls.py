from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('login/', views.login_view, name='login'),
]