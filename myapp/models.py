from django.db import models

# Create your models here.
# ! RELACION MUCHOS A MUCHOS = Teacher VS Subject
# class Teacher(models.Model):
#   teacherID = models.IntegerField(primary_key=True)
#   qualification = models.CharField(max_length=50)
#   email = models.EmailField(max_length=50)

# class Subject(models.Model):
#   subjectcode = models.IntegerField(primary_key = True)
#   name = models.CharField(max_length=30)
#   credits = models.IntegerField()
#   teacher = models.ManyToManyField(Teacher)

# ! RELACION UNO A MUCHOS = Teacher VS Subject
# class Teacher(models.Model):
#   TeacherID = models.IntegerField(primary_key=True)
#   subjectcode=models.ForeignKey(Subject, on_delete=models.CASCADE)
#   Qualification = models.CharField(max_length=50)
#   email = models.EmailField(max_length=50)

# class Subject(models.Model):
#   Subjectcode = models.IntegerField(primary_key = True)
#   name = models.CharField(max_length=30)
#   credits = models.IntegerField()
