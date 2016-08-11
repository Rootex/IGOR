from django.db import models


class Puzzle(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=255)
