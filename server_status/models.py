from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    is_up = models.BooleanField(default=True)
    checked_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
