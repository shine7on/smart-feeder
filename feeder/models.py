from django.db import models

# Create your models here.
class FeedingTime(models.Model):
    datetime = models.DateTimeField(blank=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.datetime}"