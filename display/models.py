from django.db import models

class Page(models.Model):
    url = models.CharField(max_length = 20)
    title = models.CharField(max_length = 100)
        