from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length= 200,null=True,blank=True)
    age=models.IntegerField()
    desc=models.TextField(default="This is the description of a person, you can change if you want",null=True,blank=True)

    def __str__(self):
        return self.name
