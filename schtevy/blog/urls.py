from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    # TODO This page should contain a intro to the post and a navigation to the post home and blog stats
    # /blog/
    path("", views.blog_home, name="blog_home"),

    # /blog/stats/
    path("stats/", views.blog_stats, name="blog_stats"),

    # /blog/authors/
    path("author/", views.authors_home, name="authors_home"),
    
    path("author/<nickname>/", views.author, name="author"),


    # /blog/post/
    path("post/", views.posts_home, name="posts_home"),

    # e.g. /blog/post/5/
    path("post/<int:post_id>/", views.post, name="post"),
    # https://docs.djangoproject.com/en/4.2/intro/overview/#design-your-urls
    # path("articles/<int:year>/", views.year_archive),
    # path("articles/<int:year>/<int:month>/", views.month_archive),
    # path("articles/<int:year>/<int:month>/<int:pk>/", views.article_detail),

    # e.g. /blog/post/5/stats
    path("post/<int:post_id>/stats/", views.post_stats, name="post_stats"),
]