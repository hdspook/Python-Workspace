from django.db import models

# Create your models here.

class Merge(models.Model):
    file_names = models.TextField()
    output_file_name = models.CharField(max_length=200)

