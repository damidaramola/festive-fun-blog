from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.model import User
from cloudinary.model import CloudinaryField

# Create model for each blog post 

STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.Slugfield()
    tags = TaggableManager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_articles')
    body = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    exerpt = models.TextField(blank=True)
    created_on = models.DateTimeFeild(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    claps = models.ManyToMantField(User, related_name='blog_claps', blank=True)
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.title
    
    def number_of_claps(self):
        return self.claps.count()
    
