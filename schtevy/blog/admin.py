from django.contrib import admin

from .models import Author
admin.site.register(Author)

from .models import Article
admin.site.register(Article)
