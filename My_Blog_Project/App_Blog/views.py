from dataclasses import fields
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView,\
    TemplateView, DeleteView
from .models import Blog,Comment, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def blog_list(request):
    dict = {}
    return render(request, 'App_Blog/blog_list.html', context=dict)

class CreateBlog(CreateView, LoginRequiredMixin):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = '__all__'