
from django.urls import path, include, re_path

from . import views



urlpatterns = [
    path('search/', views.search, name='search'),
    path('posts/<category_slug>/<slug:slug>/', views.detail, name='post_detail'),
    path('<slug:category_slug>/<slug:slug>/', views.detail, name='post_detail'),         #to slug our url link to be similar to each blog post and the category to which the post  belongs should be before thr post slug
    path('<slug:slug>/', views.category, name='category_detail'),           #slug link for category section
    path('categories/', views.category_list, name='category_list'),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
] 