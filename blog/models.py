from django.conf import settings
from django.db import models
from django.utils import timezone

#モデル名:Post
#models.Model:ポストがDjango ModelでDjangoがデータベースに保存すべきものだと分かるように
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#他のモデルへのリンク
    title = models.CharField(max_length=200)#文字数を200文字に制限のフィールド
    text = models.TextField()#文字制限なしのフィールド
    created_date = models.DateTimeField(default=timezone.now)#日時と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)#日時と時間のフィールド

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title