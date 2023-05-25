from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post, Category        #we are importing our blog from our backend so we can display it in our front end

# Create your views here.
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)          #pull the post from the database
    return render(request,'core/frontpage.html', {'posts':posts})        #Use this to render the html o our browser      the dictionarry that contaains the post 

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request,  'core/contact.html')

def category(request):
    categories = Category.objects.all
    return render(request, 'blog/categories.html', {'categories':categories})

#remember to add category and contact us here

def robots_txt(request):                        #so bots cant open our admin
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")