from django.contrib import admin

from .models import Post, Category, Comment

class CommentItemInline(admin.TabularInline):           #creating a table where we can view and edit comments under our posts in admin
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):                      # WE want  to  arrange our post in our admin database by title, slug, created_at etc
    search_fields = ['title', 'intro', 'body']
    list_display = ['title', 'slug' , 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at','status']            # to add the filter navigation for where we can see categories of post and created at
    inlines = [CommentItemInline]

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}           #so that whenever we updaate title for our categories, the slug will be automatuucally update

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']




admin.site.register(Post, PostAdmin)           #To register new section under our blog to store its data in admin 
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Comment, CommentAdmin)      

