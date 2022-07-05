from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    '''
    Model for posts
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_zih4gk', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
