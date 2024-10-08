from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect

from urlsAndViews.department.models import Department


def index(request):
    return HttpResponse(f"<h1>It's work</h1>")


def department_home(request):
    return render(request, "department/index.html")


def view_department_by_id(request, pk):
    try:
        department = Department.objects.get(pk=pk)
        return HttpResponse(f"<h1>Department: {department.name}</h1>")
    except Department.DoesNotExist:
        raise Http404("Department not found")


def view_department_by_id_and_slug(request, pk, slug):
    department = get_object_or_404(Department, pk=pk, slug=slug)
    return render(request, "department/detail.html", {"department": department})


def department_list(request):
    departments = Department.objects.all()  # Fetch all departments from the database
    return render(request, 'department/department_list.html', {'departments': departments})


def add_department(request):
    if request.method == 'POST':
        department_name = request.POST.get('name')
        if department_name:
            Department.objects.create(name=department_name)
            return redirect('department_list')
    return render(request, 'department/add_department.html')


def custom_page_not_found_view(request, exception):
    message = str(exception)
    return render(request, "404.html", {"message": message}, status=404)

