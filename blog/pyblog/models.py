from django.db import models

# Create your models here.
class Article(models.Model):
    def __str__(self):
        return self.article_title

    article_title = models.CharField(max_length=50, default="Article title")
    article_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('Date published')
    likes = models.IntegerField(default=0)


class Comment(models.Model):
    def __str__(self):
        return self.comment_text

    related_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)