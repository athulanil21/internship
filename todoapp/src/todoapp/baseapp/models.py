from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=128)
    priority = models.IntegerField()
    status = models.IntegerField()
    created = models.DateField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
