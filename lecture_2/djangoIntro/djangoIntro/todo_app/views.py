from django.shortcuts import render

from djangoIntro.todo_app.models import Task


def index(request):
    title_filter = request.GET.get("title_filter", "")

    tasks = Task.objects.filter(title__icontains=title_filter)

    context = {
        "title_filter": title_filter,
        "tasks": tasks
    }

    return render(request, 'tasks/index.html', context)
