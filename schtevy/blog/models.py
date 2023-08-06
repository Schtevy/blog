from django.db import models

class article(models.Model):
    title = models.CharField(max_length=25)
    pub_date = models.DateTimeField("date published")


class author(models.Model):
    email = models.CharField(max_length=50)