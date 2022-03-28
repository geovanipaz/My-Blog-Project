from dataclasses import fields
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView,\
    TemplateView, DeleteView
from .models import Blog,Comment, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
# Create your views here.

def blog_list(request):
    dict = {}
    return render(request, 'App_Blog/blog_list.html', context=dict)

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'
    queryset = Blog.objects.order_by('-publish_date')


class CreateBlog(CreateView, LoginRequiredMixin):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title','blog_content','blog_image')
    
    def form_valid(self, form):
        blog_obg = form.save(commit=False)
        blog_obg.autor = self.request.user
        title = blog_obg.blog_title
        blog_obg.slug = title.replace(" ","-")+ "-" +str(uuid.uuid4())
        blog_obg.save()
        return HttpResponseRedirect(reverse('index'))