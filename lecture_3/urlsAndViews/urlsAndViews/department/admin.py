from django.contrib import admin

from urlsAndViews.department.models import Department


# Register your models here.

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "description")
    search_fields = ('name',)
