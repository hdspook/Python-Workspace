from django.db import models

# Create your models here.

class Convert(models.Model):
    file_name = models.CharField(max_length=200)
    output_file_name = models.CharField(max_length=200)

