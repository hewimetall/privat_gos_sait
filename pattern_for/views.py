from django.shortcuts import render
from markdownx.utils import markdownify
from .models import pattern_for
from .models import categoy
from django.http import HttpResponse
from django.views.generic import ListView
# Create your views here.

def test(request,test):
    return HttpResponse(print(request.session))

def post_titile(request,cat,slug):
    if (cat=='for_you' or cat=='for_gos' or cat =='for_biznes'):
        posts = pattern_for.objects.get(slug=slug,categoy=cat)
        print (" MY PRIIIINT  {}".format(posts))
        posts.text=markdownify(posts.text)
        return render(request, 'pattern_for/post.html', {'posts': posts})
    return HttpResponse("404 not found")


def post_list(request,reder):
    if (reder == 'for_you' or reder == 'for_gos' or reder =="for_biznes"):
        posts = pattern_for.objects.filter(categoy =reder)
        return render(request,'pattern_for/index.html',context={'name':request,'post':posts})
    return HttpResponse("404 not found")