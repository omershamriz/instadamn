from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.base import Model
from django.db.models.fields import DateField
from django.db.models.signals import post_save
from post.models import Post


# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(max_length=150, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="profile_picture", blank=True, null=True, verbose_name='Picture', default="default-user.png")
    favorite = models.ManyToManyField(Post, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 300, 300

        if self.image:
            image = Image.open(self.image.path)
            image.thumbnail(SIZE, Image.LANCZOS)
            image.save(self.image.path)

    def __str__(self):
        return f'{self.user.username} - Profile'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)
