from django.shortcuts import render
from markdownx.utils import markdownify
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .form import *
from .models import Contact_bd
from cart.cart import Cart
# Create your views here.
def split_f(sp):
    l=list(sp)
    lr=''
    for i in l:
        lr=lr+" \n"+i
    return lr

def test(request,test):
    return HttpResponse(print(request.session))

def contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print ("tests")
            cart = Cart(request)
            l = [s['product'].name for s in cart]
            cd =  form.cleaned_data
            Contact_bd.objects.create(name=cd['name'],
                    email = cd['email'],
                    phone = cd['phone'],
                    text  = cd['text'],
                    select_list  = split_f(l)
                    )
            return render(request,'form/post.html',context={'name':request})
    form=ContactForm()
    return render(request,'form/index.html',context={'name':request,'form':form})