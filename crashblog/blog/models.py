from django.db import models
from taggit.managers import TaggableManager

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
    title = models.CharField(max_length = 255)      #max lenght for our blog title
    slug = models.SlugField()       #The  url link of our blog posts
    intro = models.TextField()      #The first part of the blog post
    body = models.TextField()       #This is where our blog will go
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

class Comment(models.Model):                #creating a new databse to store users comments
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)         #name of commmenter
    email = models.EmailField()                     #Email of person commenting
    body = models.TextField()                       #The comment the person posted
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name                #returns the name of person who created the comments, we can also use self.email to get their email

    

