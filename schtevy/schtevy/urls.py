from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("about.urls")),
    path("blog/", include("blog.urls")),
    path("opendata/", include("opendata.urls")),
]
