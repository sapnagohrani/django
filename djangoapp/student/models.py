from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Sports(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sport = models.CharField(max_length=20)

    def __str__(self):
        return self.sport
