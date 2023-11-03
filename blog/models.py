from django.conf import settings
from django.db import models
from django.utils import timezone

#モデル名:Post
#models.Model:ポストがDjango ModelでDjangoがデータベースに保存すべきものだと分かるように
#他のモデルへのリンク
class Post(models.Model):
    #著者:ログインユーザー
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #タイトル:文字数を200文字に制限のフィールド
    title = models.CharField(max_length=200)
    #文章:文字制限なしのフィールド
    text = models.TextField()
    #作成日:日時と時間のフィールド
    created_date = models.DateTimeField(default=timezone.now)
    #作成日:日時と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
    
    