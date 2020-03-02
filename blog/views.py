from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts = Post.objects.filter().order_by('created_date')
    return render(request,'blog/post_list.html',{'posts':posts})
    
