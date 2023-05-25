from django.conf import settings
from django.conf.urls.static import static
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.contrib import admin

from core import views

from .sitemaps import CategorySitemap, PostSitemap


from core.views import frontpage, about, contact,category, robots_txt

sitemaps = {'category':CategorySitemap, 'post': PostSitemap}


urlpatterns = [path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contact'),
    path('category/', views.category, name= 'category'),
    path('', include('blog.urls')),
    path('', views.frontpage, name='frontpage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
