from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
import os

from blog.models import Post, Category
from blog.forms  import ContactForm   

# Create your views here.
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)          
    recent_posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')[:5]          #[:5]   retreiving only 5 recent post
    return render(request,'core/frontpage.html', {'posts':posts, 'recent_posts':recent_posts})        #Use this to render the html o our browser      the dictionarry that contaains the post 

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            subject = "From TobieTopia contact us form"
            messageTest = "The message"
            email_from = os.environ.get('Email_Me')
            email = form.cleaned_data['email']
            name = form.cleaned_data['name'] 
            message = form.cleaned_data['message']

            html = render_to_string('core/emails/contactform.html',{
                'name':name,
                'email':email,
                'message':message,
            })
            recipient_list = os.environ.get('Email_User')
            send_mail(subject, messageTest, email_from, [recipient_list], html_message=html)
            
            return render(request, 'core/success.html')
    else:
        form = ContactForm()

    return render(request,  'core/contact.html', {'form':form})

def category(request):              
    categories = Category.objects.all
    return render(request, 'blog/categories.html', {'categories':categories})




def robots_txt(request):                        #so bots cant open our admin
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")