from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from webapp.models import Task, Type
from webapp.forms import TaskForm
from webapp.views.projects import GroupPermissionMixin


class TaskUpdateView(GroupPermissionMixin, UpdateView):
    template_name = 'task_update.html'
    form_class = TaskForm
    model = Task

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskCreateView(GroupPermissionMixin, LoginRequiredMixin, CreateView):
    template_name = 'task_create.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

class TaskDeleteView(GroupPermissionMixin, DeleteView):
    template_name = 'task_confirm_delete.html'
    model = Task
    success_url = reverse_lazy('index')


class TaskConfirmDeleteView(GroupPermissionMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('index')


class TaskDetail(DetailView):
    template_name = 'task.html'
    model = Task









