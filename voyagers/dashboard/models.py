from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.


class Profile(models.Model):
    website = models.URLField(default='', blank=True)
    date_of_birth = models.DateField(auto_now=False)
    bio = models.TextField(default='', blank=True)
    twitter_handle = models.URLField(default='', blank=True)
    fb_handle = models.URLField(default='', blank=True)
    insta_handle = models.URLField(default='', blank=True)
    address1 = models.TextField(blank=True, default='')
    address2 = models.TextField(blank=True, default='')
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.IntegerField(blank=True, null=True)
    # photo = FileField(verbose_name=_("Profile Picture"),
    #                   upload_to=upload_to(
    #     "main.UserProfile.photo", "profiles"),
    #     format="Image", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.user.username



def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Profile(user=user)
        user_profile.save()

post_save.connect(create_profile, sender=User)


