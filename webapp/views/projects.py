from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Task, Project, User
from webapp.forms import TaskForm, ProjectForm, ProjectUserForm


class GroupPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'manager', 'dev']).exists()


class ProjectCreateView(GroupPermissionMixin, LoginRequiredMixin, CreateView):
    template_name = 'project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ProjectUpdateView(GroupPermissionMixin, LoginRequiredMixin, UpdateView):
    template_name = 'project_update.html'
    form_class = ProjectForm
    model = Project
    success_message = "Проект обновлен"
    groups = ['admin', 'manager']
    permission_required = "webapp.change_project"
    permission_denied_message = "У вас не хватает прав доступа"

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class ProjectDeleteView(GroupPermissionMixin, DeleteView):
    template_name = 'project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')


class ProjectUserAddView(GroupPermissionMixin, LoginRequiredMixin, CreateView):
    template_name = 'project_user_create.html'
    model = User
    form_class = ProjectUserForm

    def get_success_url(self):
        return reverse('project_index')


class ProjectUserDeleteView(GroupPermissionMixin, DeleteView):
    template_name = 'project_user_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')


class ProjectUserConfirmDeleteView(GroupPermissionMixin, TemplateView):
    template_name = 'project_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = get_object_or_404(Project, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(Project, pk=kwargs['pk'])
        user.delete()
        return redirect('project_index')


class ProjectConfirmDeleteView(GroupPermissionMixin, TemplateView):
    template_name = 'project_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Task, pk=kwargs['pk'])
        project.delete()
        return redirect('project_index')


class ProjectDetail(DetailView):
    template_name = 'project.html'
    model = Project


