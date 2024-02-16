from django.db import models

# Create your models here.
class School(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)

    def __str__(self):
        return self.sname
    
class Student(models.Model):
    stid=models.IntegerField(primary_key=True)
    stname=models.CharField(max_length=100)
    stage=models.IntegerField()
    sname=models.ForeignKey(School,on_delete=models.CASCADE,related_name='Students')

    def __str__(self):
        return self.stname

