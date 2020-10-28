from django.db import models

# Create your models here.

'''
Model class to store the details of merged files
'''
class Merge(models.Model):
    file_names = models.TextField()
    output_file_name = models.CharField(max_length=200)
    output_file_path = models.CharField(max_length= 250)
    merge_status = models.CharField(max_length = 200)

