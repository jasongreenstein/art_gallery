from django.db import models


# Create your models here.


class Art(models.Model):
    title = models.CharField(max_length=200)
    series = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(default="default.png", blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
