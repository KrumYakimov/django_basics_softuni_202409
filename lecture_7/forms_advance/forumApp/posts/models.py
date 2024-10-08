from django.db import models

from forumApp.posts.choices import LanguageChoices
from forumApp.posts.validators import BadLanguageValidator


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(
        validators=(
            BadLanguageValidator(),
        )
    )
    author = models.CharField(max_length=30)
    # author = models.ForeignKey(
    #     to="Author",
    #     on_delete=models.CASCADE
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(
        max_length=20,
        choices=LanguageChoices.choices,
        default=LanguageChoices.OTHER
    )


# class Author(models.Model):
#     name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.name


