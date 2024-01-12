from . import views
from django.urls import path

urlpatterns = [
    path("", views.view_poems, name="poems"),
    path("/edit_comment/<int:comment_id>",
         views.comment_edit, name='comment_edit'),
    path("/delete_comment/<int:comment_id>",
         views.comment_delete, name='comment_delete'),
]