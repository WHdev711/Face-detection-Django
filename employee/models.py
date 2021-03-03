from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_image = models.FileField(upload_to='images/')

