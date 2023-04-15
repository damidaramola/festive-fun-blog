from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create model for each blog post with tags 

STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    tags = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_articles')
    body = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    claps = models.ManyToManyField(User, related_name='blog_claps', blank=True)
    
    class Meta:
        ordering = ['-created_on']
           
    def __str__(self):
        return self.title

    def number_of_claps(self):
        return self.claps.count()
    
        
class Comment(models.Model):
    user_name = models.CharField(max_length=80)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)    
    accepted = models.BooleanField(default=False)
     
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return f"Comment {self.body} written by {self.user_name}"
    
