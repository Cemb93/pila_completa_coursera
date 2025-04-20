from django.db import models

class Booking(models.Model):
  first_name = models.CharField(max_length=200)
  reservation_date = models.DateField()
  reservation_slot = models.SmallIntegerField(default=10)

  def __str__(self): 
    return self.first_name


# Add code to create Menu model
class Menu(models.Model):
  name = models.CharField(max_length=200) 
  price = models.IntegerField(null=False) 
  menu_item_description = models.TextField(max_length=1000, default='') 

  def __str__(self):
    return self.name

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
