from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import ModelForm
from .forms import Profileform
from .models import Profile
from Product.models import Cart
# Create your views here.

def Registerpage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            cart = Cart(user=user)
            cart.save()
            return redirect('/')    
    context={
        'form':form,
    }
    return render(request,'UserManagement/register.html',context)



@login_required
def CreateProfile(request):
    form = Profileform()
    if request.method == "POST":
        form = Profileform(request.POST,request.FILES)
    if form.is_valid():
        profile_object =form.save(commit=False)
        profile_object.user =request.user
        profile_object.save()
        return redirect('/')
    context ={
        'form':form,
    }
    return render(request,'UserManagement/create_profile.html',context)    


@login_required
def ViewProfile(request):
    profile=Profile.objects.get(user=request.user)    
    context ={
        'profile':profile,
    }
    return render(request,'UserManagement/view_profile.html',context)    