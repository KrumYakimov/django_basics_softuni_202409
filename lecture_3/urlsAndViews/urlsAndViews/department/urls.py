from django.urls import path

from urlsAndViews.department import views

urlpatterns = [
    path("", views.index, name="home"),
    path("home", views.department_home, name="home"),
    path("<int:pk>/", views.view_department_by_id, name="department-name"),
    path('<uuid:pk>/<slug:slug>/', views.view_department_by_id_and_slug, name='department-detail'),
    path('add/', views.add_department, name='add_department'),
    path('list/', views.department_list, name='department_list'),
]
