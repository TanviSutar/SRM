from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post


# Create your views here.
@login_required
def home(request):
    context = {
        'title':'Blog Home',
        'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html',context)