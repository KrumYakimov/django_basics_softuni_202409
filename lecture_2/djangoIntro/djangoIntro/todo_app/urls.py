from django.urls import path

from djangoIntro.todo_app import views

urlpatterns = [
    path("", views.index, name="index")
]