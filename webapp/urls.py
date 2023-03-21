from django.urls import path
from webapp.views.tasks import TaskDetail, TaskUpdateView, TaskDeleteView, TaskConfirmDeleteView, TaskCreateView
from webapp.views.base import IndexView, ProjectView
from webapp.views.projects import ProjectDetail, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, ProjectUserAddView, ProjectUserDeleteView


urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('task/add/', TaskCreateView.as_view(), name='task_add'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/confirm_delete/', TaskDeleteView.as_view(), name='task_confirm_delete'),
    path('project/', ProjectView.as_view(), name='project_index'),
    path('project/add/', ProjectCreateView.as_view(), name='project_add'),
    path('project/<int:pk>', ProjectDetail.as_view(), name='project_detail'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/confirm_delete/', ProjectDeleteView.as_view(), name='project_confirm_delete'),
    path('project/user_add', ProjectUserAddView.as_view(), name='project_user_add'),
    path('project/<int:pk>/user_delete/', ProjectUserDeleteView.as_view(), name='project_user_delete'),
    path('project/<int:pk>/user_confirm_delete/', ProjectUserDeleteView.as_view(), name='project_user_confirm_delete'),
]

