from django.contrib import admin

from .models import Author
admin.site.register(Author)

from .models import BlogPost
admin.site.register(BlogPost)
