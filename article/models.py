from django.db import models

class Message(models.Model):
    message = models.CharField(max_length=255)

    def __str__(self):
        return "<{0}>".format(self.message)