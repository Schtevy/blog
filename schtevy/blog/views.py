from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import BlogPost, Author

from django.urls import reverse
from django.views import generic

def blog_home(request):
    return render(request, "home.html", {
        "key": "value",
    })


def blog_stats(request):
    # TODO gather insights and then make it transparent here
    avg_num_of_post_read_by_visitor = 1

    return render(request, "stats.html", {
        "avg_num_of_post_read_by_visitor": avg_num_of_post_read_by_visitor,
    })

def authors_home(request):
    authors = get_list_or_404(Author.objects)

    return render(request, "authors/home.html", {
        "authors": authors,
    })


def author(request, nickname):
    author = get_object_or_404(Author, pk=nickname)

    return render(request, "authors/author.html", {
        "nickname": author.nickname,
    })


def posts_home(request):
    latest_blog_posts = get_list_or_404(BlogPost.objects.order_by("-pub_date")[:5])

    return render(request, "posts/home.html", {
        "latest_blog_posts": latest_blog_posts,
    })


def post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)  
    return render(request, "posts/post.html", {
        "post_id": post_id,
        "post_pub_date": post.pub_date,
        "post_mod_date": post.mod_date,
        "post_title": post.title,
        "post_content": post.content,
    })


def post_stats(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)

    # TODO add logic to get additional statistics to the post. 
    # In the backend the stats should be stored and updated regularly. 
    # The stats are static and the user can not do anything (it is not a data monitoring!)

    return render(request, "posts/stats.html", {
        "post_id": post_id,
        "post_pub_date": post.pub_date,
        "post_mod_date": post.mod_date,
        "post_title": post.title,
        "post_content": post.content,
    })