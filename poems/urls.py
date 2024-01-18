from . import views
from django.urls import path

urlpatterns = [
    path("", views.view_poems, name="poems"),
	path("add_poem/", views.add_poem, name="add_poem"),
    path(
		"view_poem/<int:poem_id>",
		views.view_poem,
		name='view_poem'
	),
    path(
		"edit_comment/<int:comment_id>",
		views.edit_comment,
		name='comment_edit'
	),
    path(
		"delete_comment/<int:comment_id>",
		views.delete_comment,
		name='comment_delete'
	),
	path(
		"accounts/", 
		include("allauth.urls")),
]