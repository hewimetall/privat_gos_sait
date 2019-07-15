from django.shortcuts import render ,redirect
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
    if (cat=='for_gos' or cat =='for_biznes'):
        posts = pattern_for.objects.get(slug=slug,categoy=cat)
        posts.text=markdownify(posts.text)
        return render(request, 'pattern_for/post.html', {'posts': posts})
    return HttpResponse("404 not found")


def post_list(request,reder):
    if (reder == 'for_gos' or reder =="for_biznes" or reder == 'for_you' ):
        posts = pattern_for.objects.filter(categoy =reder)
        return render(request,'pattern_for/index.html',context={'name':request,'post':posts})
    return HttpResponse("404 not found")

