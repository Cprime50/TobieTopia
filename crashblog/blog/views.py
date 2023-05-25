from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect , render

from .forms import CommentForm
from .models import Post, Category
from taggit.models import Tag


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)               #if someone clicks our blog post it will take them to our details.html, which has acces to our Postclass inn our models.py, post.ACTIVE so this apply only to active posts, only active posts will display

    if request.method == 'POST':
        form = CommentForm(request.POST)                #we are telling django to save the comments people post under the commentform   class

        if form.is_valid():
            comment = form.save(commit=False)           #to add to the  database
            comment.post = post
            comment.save()

            return redirect('post_detail', slug = slug)
    else:
        form = CommentForm()

    form = CommentForm()                                    #this will display our comment section in the front end

    return render(request, 'blog/detail.html', {'post':post, 'form':form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category':category, 'posts':posts})          #post here is added so only active posts display in category


def category_list(request, slug):       #creating category list view
    
    categories = get_object_or_404(Category, slug=slug)
    
    return render(request, 'blog/categories.html', {'categories':categories} )

def search(request):                                    #so user can search for a post using tyhr seach query
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter (Q(title__icontains = query) | Q(intro__icontains=query) | Q(body__icontains=query))         #This is so u can searcg for keywords contained in any post body or into                  #the Q here is so the users search isn't case sensitive

    return render(request, 'blog/search.html', {'posts':posts, 'query': query})