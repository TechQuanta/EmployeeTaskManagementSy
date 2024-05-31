from django.urls import path
from . import views

urlpatterns = [
    path("", views.HOME, name="HOME"),
    path("CONTACT", views.CONTACT, name="CONTACT"),  # Remove the leading slash
    path("Registrationofemployee", views.REGIEMP, name="REGIEMP"),
    path("ADMINLOGIN", views.ADMINLOGIN, name="ADMINLOGIN"),
    path("ABOUT", views.ABOUT, name="ABOUT"),
    path('Tasks', views.assign_task, name='Task'),
    path("employeesignuplogin", views.employeesignuplogin,
         name="employeesignuplogin"),
    path("REGIEMP", views.REGIEMP, name="REGIEMP"),
    path("Developers", views.DEV, name="Developers"),
    path("REGIDMENT", views.REGIDMENT, name="REGIDMENT"),
    path("ADMINLOGIN/AdminDashboard",views.AdminDashboard,name="AdminDashboard"),
    path('AdminDashboard/assigned-tasks/', views.assigned_tasks, name='assigned_tasks'),
    path('AdminDashboard/task-des/', views.task_des, name='task_des'),
    path('AdminDashboard/finished-tasks/', views.finished_tasks, name='finished_tasks'),
    path('mark_task_finished/<int:task_id>/<email>/', views.mark_task_finished, name='mark_task_finished'),
    path('AdminDashboard/task-end-dates/', views.task_end_dates, name='task_end_dates'),

    # path("AdminDashboard", views.AdminDashboard, name="AdminDashboard"),
    path('logout/', views.logout, name='logout'),
    # path('add/', views.add_employee, name='add_employee'),
    path('', views.employee_list, name='employee_list'),
    # path('edit/<int:pk>/', views.edit_employee, name='edit_employee'),
    # path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    # path('', views.employee_list, name='employee_list'),
    path('ADMINLOGIN/AdminDashboard/emplist', views.employee_list, name='employee_list'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    path('edit/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('search/', views.search_employee, name='search_employee'),
    path('Dlist/', views.department_list, name='Dlist'),
    path('search_department/', views.search_department, name='search_department'),
    path('edit_department/<int:department_id>/',
         views.edit_department, name='edit_department'),
    path('delete_department/<int:department_id>/',
         views.delete_department, name='delete_department'),
    path('AdminDashboard/TaskReport', views.TaskReport, name='TaskReport'),
    path('EMPDashboard', views.EMPDASHBOARD, name='EMPDashboard'),
    path('EMPAccount', views.EMPAccount, name='EMPAccount'),
    path('EmployeeTask', views.EmployeeTask, name='EmployeeTask'),
    # Other URL patterns...
]
