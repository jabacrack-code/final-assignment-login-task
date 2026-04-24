from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskCreationForm, AccountRegistrationForm, AccountEditForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

User = get_user_model()

class TaskLoginView(LoginView):
    template_name = 'tasks/login.html'

class TaskLogoutView(LogoutView):
    next_page = reverse_lazy('tasks:index')

class AccountRegistrationView(CreateView):
    template_name = 'tasks/signup.html'
    form_class = AccountRegistrationForm
    success_url = reverse_lazy('tasks:login')

class AccountDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'tasks/account_detail.html'

class AccountEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = AccountEditForm
    template_name = 'tasks/account_edit.html'
    success_url = reverse_lazy('tasks:account_detail')
    
    def get_object(self):
        return self.request.user

class TaskPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'tasks/password_change.html'
    success_url = reverse_lazy('tasks:account_detail')

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'tasks/account_delete.html'
    success_url = reverse_lazy('tasks:index')

    def get_object(self):
        return self.request.user


from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    tasks = Task.objects.all()
    params = {
        'tasks': tasks,
    }
    return render(request, 'tasks/index.html', params)

@login_required
def create(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        task = Task(title=title, content=content)
        task.save()
        return redirect('tasks:index')
    else:
        params = {
            'form': TaskCreationForm(),
        }
        return render(request, 'tasks/create.html', params)

def detail(request, task_id):
    task = Task.objects.get(id=task_id)
    params = {
        'task': task,
    }
    return render(request, 'tasks/detail.html', params)

@login_required
def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    if (request.method == 'POST'):
        task.title = request.POST['title']
        task.content = request.POST['content']
        task.save()
        return redirect('tasks:detail', task_id)
    else:
        form = TaskCreationForm(initial={
            'title': task.title,
            'content': task.content,
        })
        params = {
            'task': task,
            'form': form,
        }
        return render(request, 'tasks/edit.html', params)

@login_required
def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if (request.method == 'POST'):
        task.delete()
        return redirect('tasks:index')
    else:
        params = {
            'task': task,
        }
        return render(request, 'tasks/delete.html', params)
