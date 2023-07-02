from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.conf import settings
# triggred when User object is saved


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    telefon = PhoneNumberField(verbose_name="Телефон", null = False, blank = False)
    home_adress=models.TextField(verbose_name = "Адрес доставки", null = True, blank = True)
    additional_info=models.TextField(verbose_name = "Дополнительная информация", null = True, blank = True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=settings.AUTH_USER_MODEL) #User
def create_profile(sender, instance, created, **kwargs):    
    if created:
        print("User created")
        group_name = Group.objects.get(name='customers') or None
        print(group_name)
        if group_name:
            group_name.user_set.add(instance)
        