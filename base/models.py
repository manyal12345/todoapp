from django.db import models

# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    satatus = models.CharField(max_length=50, choices=[("Pending", "Pending"),("In Progress", "In Progress"),("Done", "Done")])