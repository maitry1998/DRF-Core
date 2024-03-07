from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length= 200,default="TCS")
    def __str__(self):
        return self.company_name

class Person(models.Model):
    company = models.ForeignKey(Company,null=True,blank=True,on_delete=models.CASCADE,related_name="companyname")
    name = models.CharField(max_length= 200,null=True,blank=True)
    age=models.IntegerField()
    desc=models.TextField(default="This is the description of a person, you can change if you want",null=True,blank=True)

    def __str__(self):
        return self.name
