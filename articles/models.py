from django.db import models

# Create your models here.
class Article(models.Model):
    tittle = models.CharField(max_length=100)
    content = models.TextField()
    # comment_set = 부모가 자식에게 접근할 수 있는 키 (자동 생성)

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id = 자식이 부모에게 접근할 수 있는 키 (자동 생성)

    #comment = Comment.objects.get(id=id)

