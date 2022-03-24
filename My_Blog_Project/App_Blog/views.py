from django.shortcuts import render

# Create your views here.

def blog_list(request):
    dict = {}
    return render(request, 'App_Blog/blog_list.html', context=dict)