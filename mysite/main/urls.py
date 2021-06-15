from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chef/', views.chef, name='chef'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('blog/', views.blogs, name='blog'),
    path('<int:pk>/blog-single/', views.blog_single, name='blog-single'),
    path('contact/', views.contact, name='contact'),
]
