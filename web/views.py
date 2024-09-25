from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutt(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'base.html')

@login_required
def sam(request):
    return render(request, 'sam.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['msg']
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'contact.html',{'form':form})

def item(request):
    if request.method == 'POST':
        form = Itemform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = Itemform()
    return render(request, "item.html", {'form':form})

def display(request):
    items = Item.objects.all()
    return render(request, "display.html", {'item':items})

def delt(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('display')
    
def editt(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = Itemform(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = Itemform(instance=item)
    return render(request, "edit.html",{'forms':form} )


def user_reg(request):
    if request.method == 'POST':
        form = UserRegistrationform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password2')
            user.set_password(raw_password)
            user.save()

            #save to Profile
            f_name = form.cleaned_data.get('first_name')
            l_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            pro = Profile.objects.create(user=user,f_name=f_name, l_name=l_name,username=username, email=email)
            return redirect('login')
    else:
        form = UserRegistrationform()
    return render(request, 'register.html', {'form':form})

def uslogin(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return render(request,"sam.html")
    else:
        form = UserLoginForm()
    return render(request, "login.html", {'form':form})

def uslogout(request):
    logout(request)
    return redirect('home')
