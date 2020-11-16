from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middlename = models.CharField(max_length=50, blank=True, default='')
    date_of_birth = models.DateField(auto_now=False)
    twitter_handle = models.CharField(max_length=20)
    fb_handle = models.CharField(max_length=20)
    insta_handle = models.CharField(max_length=20)
    telephone = models.CharField(max_length=13)
    website = models.CharField(max_length=50, blank=True, default='')
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=30)
    state  = models.CharField(max_length=30)
    zipcode = models.IntegerField(blank=True, null=True)
    # profile_pic = models.ImageField(upload_to='images/%m/%d')
    about = models.TextField()



    def __str__(self):
        return self.user.username



    class Meta:
        verbose_name_plural = 'profiles'