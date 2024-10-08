
from django.shortcuts import render, redirect

from forumApp.posts.forms import PostCreateForm, PostDeleteForm, PostEditForm, SearchForm
from forumApp.posts.models import Post


def index(request):
    context = {
        "my_form": ""
    }

    return render(request, 'common/index.html', context)


def dashboard(request):
    form = SearchForm(request.GET)
    posts = Post.objects.all()

    if request.method == "GET":
        if form.is_valid():
            query = form.cleaned_data["query"]
            posts = posts.filter(title__icontains=query)

    context = {
        "posts": posts,
        "form": form,
    }

    return render(request, 'posts/dashboard.html', context)


def details_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    context = {
        "post": post
    }

    return render(request, "posts/details-post.html", context)


def create_post(request):
    form = PostCreateForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("dash")

    context = {
        "form": form
    }

    return render(request, "posts/create-post.html", context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    # If the request is a POST, initialize the form with the posted data.
    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dash')
    else:
        # If it's a GET request, initialize the form with the instance.
        form = PostEditForm(instance=post)

    context = {
        "form": form,
        "post": post,
    }

    return render(request, "posts/edit-post.html", context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(request.POST or None, instance=post)

    if request.method == "POST" and form.is_valid():
        post.delete()
        return redirect("dash")

    context = {
        "form": form,
        "post": post,
    }

    return render(request, "posts/delete-post.html", context)


