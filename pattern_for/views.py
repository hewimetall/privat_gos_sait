from django.shortcuts import render ,redirect ,get_object_or_404
from markdownx.utils import markdownify
from .models import pattern_for
from .models import categoy
from django.http import HttpResponse
from django.views.generic import ListView
# Create your views here.

def my_view(request):
    # View code here...
    return redirect('/mag/')


def post_titile(request,cat,slug):
    obj=get_object_or_404(categoy,slug=cat)
    posts = pattern_for.objects.get(slug=slug,categoy=obj)
    posts.text=markdownify(posts.text)
    return render(request, 'pattern_for/post.html', {'posts': posts})

def post_list(request,reder):
    obj=get_object_or_404(categoy,slug=reder)
    posts = pattern_for.objects.filter(categoy =obj)
    return render(request,'pattern_for/index.html',context={'name':request,'post':posts})

