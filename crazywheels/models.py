from django.db import models

# Create your models here.


class MessageModel(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    image = models.ImageField()
