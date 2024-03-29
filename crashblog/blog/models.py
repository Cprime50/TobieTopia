from django.db import models
from django import forms
from taggit.managers import TaggableManager
#from django_ckeditor_5.fields import CKEditor5Field
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

from io import BytesIO
from PIL import Image
from django.core.files import File

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('-title',)       #so categories in orderd by titles
        verbose_name_plural = 'Categories'      #changing the name of the plural of category that appears in our admin portal to categories from categorys 

    def __str__(self):              #Make our categories show its title instead of just category1++
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug
    
    
    
class Post(models.Model):               #to choose whether a post should be visible or not  active and draft naigation
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)      #we want our category to connect  to  our post
    title = models.CharField(max_length = 255)      #max lenght for our blog title 255 chars
    slug = models.SlugField()       #The  url slug of our blog posts
    meta_description = models.CharField(max_length=200, blank=True)  #for google search
    intro = models.TextField()      #The intro of the blog post
    body = RichTextUploadingField()       #This is where our blog body will go
    created_at = models.DateTimeField(auto_now_add = True)  #time post is made will be automatically added
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)            #addimg images to our blog
    tags = TaggableManager()

    class Meta:
        ordering = ('-created_at',)             #'-created_at' so that our post will be orderred from the newest ones made to the old ones downward
    
    def __str__(self):                  #we have to put this here in post aswell so the posts will also show as the their title in admin portal
        return self.title
    
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)
    
    #resize image
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url 
            else:
                return 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fe7.pngegg.com%2Fpngimages%2F573%2F501%2Fpng-clipart-python-computer-icons-programming-language-font-awesome-github-angle-text.png&tbnid=3fThsVUWMFFYAM&vet=12ahUKEwjPtqTI1p6AAxVEpkwKHUKiCC4QMygKegUIARDIAQ..i&imgrefurl=https%3A%2F%2Fwww.pngegg.com%2Fen%2Fpng-nkcfs&docid=jN9bp_Ogd5lSQM&w=900&h=900&q=python%20is%20awesome%20image&ved=2ahUKEwjPtqTI1p6AAxVEpkwKHUKiCC4QMygKegUIARDIAQ'
            
    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)
        
        return thumbnail

class Comment(models.Model):                #creating a new databse to store users comments
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)       #relating each postb  and its comment with a foreign_key
    name = models.CharField(max_length=255)         #name of commmenter
    email = models.EmailField()                     #Email of person commenting
    body = models.TextField()                       #The comment the person posted
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name                #returns the name of person who created the comments, we can also use self.email to return their email

class Contact(models.Model):
    name  = models.CharField( max_length=250)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
    

       
