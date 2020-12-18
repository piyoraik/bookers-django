from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()

    def __str__(self):
        return '%s %s' % (self.title, self.body)
