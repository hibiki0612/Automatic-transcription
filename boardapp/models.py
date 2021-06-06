from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Post(models.Model):
    """投稿モデル"""
    title = models.CharField(verbose_name='タイトル', max_length=10)
    text = models.CharField(verbose_name='テキスト', max_length=100)
    mytext = models.CharField(verbose_name='マイテキスト', max_length=100)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    def __str__(self):
        return self.title 
