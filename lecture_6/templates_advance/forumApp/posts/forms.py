from django import forms

from forumApp.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].disabled = True


class SearchForm(forms.Form):
    query = forms.CharField(
        label="",
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search for a post..."
            }
        )
    )
# class PersonForm(forms.Form):
#     STATUS_CHOICE = (
#         (1, "Draft"),
#         (2, "Published"),
#         (3, "Archived")
#     )
#
#     person_name = forms.CharField(
#         max_length=10,
#         label="Add person name!",
#         widget=forms.TextInput(attrs={"placeholder": "Name"}),
#         error_messages={
#             "required": "Please enter the person's name.",
#             "max_length": "Name cannot exceed 10 characters."
#         }
#     )
#
#     age = forms.IntegerField(
#         error_messages={
#             "required": "Please provide the age.",
#             "invalid": "Enter a valid number for age."
#         }
#     )
#
#     is_lecture = forms.BooleanField(
#         required=False,
#         error_messages={
#             "invalid": "Invalid value for lecture status."
#         }
#     )
#
#     checkboxes = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple,
#         choices=STATUS_CHOICE,
#         error_messages={
#             "required": "Please select at least one status."
#         }
#     )
