from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Posts
from blog.models import Category
# Create your views here.

def homePage(request):
    # Home page content 
    posts = Posts.objects.all()
    
    data = {
        'posts':posts
    }
    return render(request,'home.html',data)

def blogPage(request):
    # load all the posts
    posts = Posts.objects.all()[:11]
    # print(posts)
    cats = Category.objects.all()
    
    data = {
        'posts' : posts,
        'cats' : cats
    }
    return render(request,'blog.html',data)

def aboutPage(request):
    # About page content 
    
    
    return render(request,'about.html',{})

def postPage(request,url):
    post = Posts.objects.get(url=url)
    cats = Category.objects.all()
    # print(postss)
    return render(request,'post.html',{'post':post,'cats':cats})
    
def categoryPage(request, url):
    cats = Category.objects.get(url=url)
    post = Posts.objects.filter(Category=cats)
    return render(request,'category.html',{'cats':cats,'post':post})