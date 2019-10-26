from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20,blank=True )
    portfolio_site = models.URLField(blank=False)

    profile_pic = models.ImageField(upload_to="profile_pics")
