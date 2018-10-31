from django.db import models

class blog(models.Model):
    title = models.CharField(max_length = 120)
    post = models.TextField(max_length = 1528)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
