from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Reaction(models.Model):

    class Sentiment(models.TextChoices):
        LIKE = "like"
        DISLIKE = "dislike"

    sentiment = models.CharField(max_length=8, choices=Sentiment)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Blog(models.Model):

    title = models.CharField(max_length=20)
    content = models.TextField()
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reaction = models.ForeignKey(
        Reaction, on_delete=models.SET_NULL, null=True, blank=True)


class Notification(models.Model):

    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
