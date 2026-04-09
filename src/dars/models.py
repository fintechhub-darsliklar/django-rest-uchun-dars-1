from django.db import models

# Create your models here.

class Universitet(models.Model):

    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} | {self.is_active}"


class Teacher(models.Model):

    name = models.CharField(max_length=255)
    mutaxasislik = models.CharField(max_length=255)
    oylik = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.mutaxasislik}"
    
class Student(models.Model):

    name = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} | {self.age}"
    

class Group(models.Model):

    name = models.CharField(max_length=255)
    universitet = models.ForeignKey(Universitet, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} | {self.teacher.name}"
    
