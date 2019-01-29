from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    class Meta:
        verbose_name = _('Profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    bio = models.TextField()
    joined_date = models.DateField(auto_now_add=True, null=True, blank=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, **kwargs):
        instance.profile.save()
