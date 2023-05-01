from django.db import models
from django.urls import reverse

# Create your models here.
class ClassRoom(models.Model):
    FR = "FRESHMAN"
    SO = "SOPHOMORE"
    JR = "JUNIOR"
    SR = "SENIOR"
    GR = "GRADUATE"
    levels = [
        (FR, 'Freshman'),
     (SO, 'Sophomore'),
     (JR, 'Junior'),
     (SR, 'Senior'),
    (GR, 'Graduate')]
    level_of_study = models.CharField(max_length=100, choices=levels)
    def __repr__(self):
        return f'{self.level_of_study}'
    def __str__(self):
        return f'{self.level_of_study}'
    
class User(models.Model):
    genders = [('M', 'Male'),
               ('F','Female')]
    
    username = models.CharField(max_length=80,null=True,blank=True)
    first_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)
    email = models.EmailField()
    birthday= models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=2, choices=genders)
    password = models.CharField(max_length=80,null=True,blank=True)
    Level_of_study = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, null=True)
    
    def __repr__(self):
        return f'{self.first_name} {self.last_name}'
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


