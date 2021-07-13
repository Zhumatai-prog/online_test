from django.db import models
from django.contrib.auth.models import User




class Dept(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отдел"

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должность"

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=False)
    email = models.EmailField(max_length=50, default=None)
    dept = models.ForeignKey(Dept, default=None, on_delete=models.DO_NOTHING)
    position = models.ForeignKey(Position, default=None, on_delete=models.DO_NOTHING)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name
