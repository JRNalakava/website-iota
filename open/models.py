from django.db import models
from chapter import models as chapter_models


# Create your models here.
class Post(models.Model):
    post_creator = models.ForeignKey(to=chapter_models.ChapterUser, on_delete=models.CASCADE)
    post_identifier = models.TextField(max_length=20)
    post_content = models.TextField(max_length=1000)


class DateDescription(models.Model):
    date_identifier = models.TextField(max_length=20)
    date_date = models.DateTimeField(null= False, default='1-1-2000')