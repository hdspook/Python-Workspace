from django.db import models

# Create your models here.

class Convert(models.Model):
    file_name = models.TextField()
    output_file_name = models.CharField(max_length=200)
    output_file_path = models.CharField(max_length= 250)
    convert_status = models.CharField(max_length = 200)

