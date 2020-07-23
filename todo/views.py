from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView # couese-36 # couese-37
from .models import TodoModel # couese-36
from django.urls import reverse_lazy

# from django.http import HttpResponse# couese-33 

# Create your views here.

# def todo(request):
#     return HttpResponse('') # couese-33 

# couese-36
class Todolist(ListView):
    template_name = 'list.html'
    model = TodoModel

# couese-37
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel

    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel

    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')