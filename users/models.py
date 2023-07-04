from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(default='profile_pics/default.jpg', upload_to='profile_pics/') 
    email = models.EmailField(max_length=200, null= True)
    facebook_link = models.CharField(max_length=200, null= True)
    github_link = models.CharField(max_length=200, null= True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
     

