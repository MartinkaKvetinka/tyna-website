from django.db import models


class Content(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=10000)

    def __str__(self):
        return self.name + ': ' + self.text
