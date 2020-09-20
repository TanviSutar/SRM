from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data.get('first_name')
            messages.success(request,f'Welcome to BlogBuzz, {fname.capitalize()}!!!')
            return redirect('blog_home')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
