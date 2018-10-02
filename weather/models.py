from django.db import models

# Create your models here.

class Citys(models.Model):
    cname=models.TextField(max_length=30,default="")