from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification, Reaction


@receiver(post_save, sender=Reaction)
def create_notification(instance, sender, created, **kwargs):
    print("called")
    if created:
        Notification.objects.create(
            receiver=instance.user,
            message=f"{instance.sentiment}d your post"
        )