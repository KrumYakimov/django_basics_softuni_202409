from django.urls import path, include

from forumApp.posts.views import dashboard, index, create_post, delete_post, edit_post, details_post

urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", dashboard, name="dash"),
    path("create-post/", create_post, name="create-post"),
    path("<int:pk>/", include([
        path("delete-post/", delete_post, name="delete-post"),
        path("details-post", details_post, name="details-post"),
        path("edit-post/", edit_post, name="edit-post")
    ]))
]
