from django.db import models


class Familiar(models.Model):
    name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    birth= models.DateField(auto_now_add=True)
    



