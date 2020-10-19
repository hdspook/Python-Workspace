from django.db import models


class Teams(models.Model):
    team_name = models.CharField(max_length=200)
    formed_on = models.DateTimeField('date published')

    def __str__(self):
        return self.team_name


class Developers(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, default=None)
    dev_name = models.CharField(max_length=200)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.dev_name