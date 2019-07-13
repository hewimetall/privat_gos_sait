from django.shortcuts import render
from markdown import markdown
from .models import about_company,item_block,list_menu
from django.http import HttpResponse
# Create your views here.
def content_render(request):
    response = HttpResponse()
    items_block= item_block.objects.all()
    response.write(render(request,'about_company/block-img.html',context={'name':request,'block':items_block}).content)

  #  post=about_company.objects.all()
  # response.write(render(request,'about_company/block_slider.html',context={'name':request,'post':post}).content)

    lists_menu= list_menu.objects.all()
    response.write(render(request,'about_company/glob_meny.html',context={'name':request,'list_menu':lists_menu}).content)

    return HttpResponse(render(request,'about_company/index.html',context={'post':str(response.content.decode('utf-8'))}).content)
