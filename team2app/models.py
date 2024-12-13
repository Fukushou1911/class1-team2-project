from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)  # 投稿タイトル
    content = models.TextField()  # 投稿内容
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # 関連する投稿
    text = models.TextField()  # コメント内容
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時

    def __str__(self):
        return f"Comment on {self.post.title} by {self.created_at}"
