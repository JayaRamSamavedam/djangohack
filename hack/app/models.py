from django.db import models

from django.contrib.auth.models import User


class Room(models.Model):
    room_no=models.CharField(max_length=20,primary_key=True,default=None)
    def __str__(self):
        return str(self.room_no)
# Create your models here.

class Team(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    team_name=models.CharField(max_length=20)
    def __str__(self):
        return str(self.team_name)
    
class Student(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    id=models.BigIntegerField(primary_key=True)
    name=models.CharField(max_length=20,default=id)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

class Session(models.Model):
    session_no=models.IntegerField()
    Attendence=models.BooleanField(null=True)
    Review=models.BooleanField(null=True)
    def __str__(self):
        return str(self.session_no)

class Attendence(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    session = models.ForeignKey(Session,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE,default=None)

    
class Review(models.Model):
    review_no=models.IntegerField(default=0)
    session = models.ForeignKey(Session,on_delete=models.CASCADE)
    review_marks = models.IntegerField(default=0)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    # attendence= models.ForeignKey(Attendence,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.review_no)

class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20,default="")
    def __str__(self):
        return str(self.id)
