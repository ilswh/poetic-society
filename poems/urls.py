from . import views
from django.urls import path

urlpatterns = [
	path("", views.view_poems, name="poems"),
	path("add_poem/", views.add_poem, name="add_poem"),
	path("edit_poem/<int:poem_id>", views.edit_poem, name="edit_poem"),
	path("delete_poem/<int:poem_id>", views.delete_poem, name="delete_poem"),
	path("view_poem/<int:poem_id>", views.view_poem, name='view_poem'),
]
