from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.conf import settings
# triggred when User object is saved

@receiver(post_save, sender=settings.AUTH_USER_MODEL) #User
def create_profile(sender, instance, created, **kwargs):
    print("User created")
    if created:
        user=instance
        group_name = Group.objects.get(name='customers') or None

        print(group_name)
        if group_name:
            group_name.user_set.add(user)