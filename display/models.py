from django.db import models

class Article(models.Model):
    post_id = models.IntegerField()
    group_id = models.IntegerField()
    url = models.CharField(max_length=20)
    title = models.CharField(max_length=40)
    content = models.TextField()
    insert_date = models.DateTimeField()
    update_date= models.DateTimeField()

class Group(models.Model):
    group_id = models.IntegerField()
    content_name = models.CharField(max_length=40)     