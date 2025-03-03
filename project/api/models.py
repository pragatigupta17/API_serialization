from django.db import models


# Create your models here.
'''class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contat=models.IntegerField(max_length=20)
    stu_city=models.CharField(max_length=50)
    def __str__(self):
         return self.stu_name'''

class Student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contat=models.IntegerField(max_length=20)
    stu_city=models.CharField(max_length=50)
    def __str__(self):
         return self.stu_name
class Employ(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_email=models.EmailField()
    emp_contat=models.IntegerField(max_length=20)
    emp_city=models.CharField(max_length=50)
    def __str__(self):
         return self.emp_name
class Client(models.Model):
    cnt_name=models.CharField(max_length=50)
    cnt_email=models.EmailField()
    cnt_contat=models.IntegerField(max_length=20)
    cnt_city=models.CharField(max_length=50)
    def __str__(self):
         return self.cnt_name
class Teacher(models.Model):
    tch_name=models.CharField(max_length=50)
    tch_email=models.EmailField()
    tch_contat=models.IntegerField(max_length=20)
    tch_city=models.CharField(max_length=50)
    def __str__(self):
         return self.tch_name
class School(models.Model):
    sch_name=models.CharField(max_length=50)
    sch_email=models.EmailField()
    sch_contat=models.IntegerField(max_length=20)
    sch_city=models.CharField(max_length=50)
    def __str__(self):
         return self.sch_name


