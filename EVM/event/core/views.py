from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from item.models import Category,Item

from .forms import SignupForm

def index(request):
    items=Item.objects.filter(is_booked=False)[0:6]
    categories=Category.objects.all()
    return render(request, 'core/index.html',{
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request,'core/contact.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form=SignupForm()
    
    return render(request,'core/signup.html',{
        'form':form
    })

def management(request):
    Customer=User.objects.all()
    context={'Customer':Customer}
    return render(request,'core/management.html',context)

def sample(request):
    return render(request,'/sample')
@login_required
def bookings(request):
    items=Item.objects.filter(is_book=True)[0:6]
    categories=Category.objects.all()
    return render(request, 'core/bookings.html',{
        'categories': categories,
        'items': items,
    })

@login_required
def book_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.is_book = True
    item.save()
    return redirect('/')
def cancel_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.is_book = False
    item.save()
    return redirect('/')