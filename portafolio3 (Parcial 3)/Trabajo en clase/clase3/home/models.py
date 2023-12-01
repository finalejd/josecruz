from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

#Usuario de prueba
class UserPrueba(models.Model):
    first_name = models.CharField(max_length=16, default="Gost User", blank=True, null=True)
    last_name = models.CharField(max_length=16, default="Phantom User")
    age = models.IntegerField(default=1)
    weight = models.FloatField(default=1.5)
    status = models.BooleanField(default=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name
     
#Modelo para profile
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=32, default="Generic User", blank=True, null=True)
    age = models.IntegerField(default=0, blank=True, null=True)
    email=models.EmailField(default="user@gmail.com",  blank=True, null=True)
    bio = models.CharField(max_length=256, default="I love this APP",  blank=True, null=True)
    status=models.BooleanField(default=True)

    def __str__(self):
     return self.name
    

#Guarda el usuario en la bd
@receiver(post_save, sender=User)
def update_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

