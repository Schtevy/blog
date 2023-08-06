from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # https://docs.djangoproject.com/en/4.2/intro/overview/#design-your-urls
    # path("articles/<int:year>/", views.year_archive),
    # path("articles/<int:year>/<int:month>/", views.month_archive),
    # path("articles/<int:year>/<int:month>/<int:pk>/", views.article_detail),
]