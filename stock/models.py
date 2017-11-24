from django.db import models

# Create your models here.

class Item(models.Model):
    cd = models.TextField()
    nm = models.TextField()
    bizcd = models.TextField()
    biznm = models.TextField()
