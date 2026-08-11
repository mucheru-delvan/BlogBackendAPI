from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Blog API Admin"
admin.site.site_title = "Blog API Admin Portal"
admin.site.index_title = "Welcome to the Blog API Portal"
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]
