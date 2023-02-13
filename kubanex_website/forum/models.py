from django.db import models
from django.contrib.auth.models import User

# Models we need to fully get forum mvp working:
# - Profile (one-to-one with User, but have additional personal info)
# - Thread (a collection of related posts)
# - Post (may contain a few images and text (in markdown))
# - Comment (only text)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)

class Thread(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
