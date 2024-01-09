from . import views
from django.urls import path

urlpatterns = [
    path("", views.my_blog, name="blog"),
    path("test/", views.test_route, name="test"),
]