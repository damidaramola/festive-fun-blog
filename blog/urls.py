from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [  
 path('', views.home_list, name='homepage'),
 path('about/', views.about, name='about_page'),
 path('<slug:post>/', views.SinglePost.as_view(), name='single_post'),
 path('clap/<slug:post>', views.ClapPosts.as_view(), name='clap_posts'),

]