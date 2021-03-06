from django.db import models

class Exam(models.Model):
    Question=models.CharField(max_length=100)
    Option1=models.CharField(max_length=20)
    Option2=models.CharField(max_length=20)
    Option3=models.CharField(max_length=20)
    Option4=models.CharField(max_length=20)
    Answer=models.CharField(max_length=20)
    
    class Meta:
        db_table='questionbank'

class Newuser(models.Model):
    Username=models.CharField(max_length=100)
    Email=models.CharField(max_length=20)
    Passwrd=models.CharField(max_length=20)
    
    
    class Meta:
        db_table='users'
    

class QuizHistory(models.Model):
    Email=models.CharField(max_length=20)
    Question=models.CharField(max_length=100)
    Answer=models.CharField(max_length=50)
    YourAnswer=models.CharField(max_length=50)
    Time=models.CharField(max_length=20)

    class Meta:
        db_table='quiz_history'