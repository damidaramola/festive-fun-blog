from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [  
 path('', views.home_list, name='homepage'),
 path('<slug:post>/', views.single_post, name='single_post'),
]