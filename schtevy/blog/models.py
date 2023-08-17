from django.db import models

class Author(models.Model):
    nickname = models.CharField(max_length=50, primary_key=True)
    email = models.CharField(max_length=50)

    class Meta:
        ordering = ["nickname"]
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.nickname

class BlogPost(models.Model):
    authors = models.ManyToManyField(Author)

    title = models.CharField(max_length=25)
    content = models.TextField()

    pub_date = models.DateTimeField("date published")
    mod_date = models.DateTimeField("date modified")

    class Meta:
        ordering = ["mod_date"]
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title   