from django.db import models
from multiselectfield import MultiSelectField


from student.models import *

class Course(models.Model):
   course_name = models.CharField(max_length=50)

   dept = models.ManyToManyField(Dept)
   position = models.ManyToManyField(Position)

   class Meta:
        verbose_name = "Тесты"
        verbose_name_plural = "Тесты"

   def __str__(self):
        return self.course_name

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=False)
    question = models.CharField(max_length=600)

    option1 = models.CharField(max_length=200, null=True, blank=True)
    option2 = models.CharField(max_length=200, null=True, blank=True)
    option3 = models.CharField(max_length=200, null=True, blank=True)
    option4 = models.CharField(max_length=200, null=True, blank=True)
    option5 = models.CharField(max_length=200, null=True, blank=True)

    # Вопросы в которых нужно быбрать картинку
    picture1 = models.ImageField(upload_to='static/questions-picture', null=True, blank=True)
    picture2 = models.ImageField(upload_to='static/questions-picture', null=True, blank=True)
    picture3 = models.ImageField(upload_to='static/questions-picture', null=True, blank=True)
    picture4 = models.ImageField(upload_to='static/questions-picture', null=True, blank=True)
    picture5 = models.ImageField(upload_to='static/questions-picture', null=True, blank=True)

    #Вопросы в которых должны вводить данные
    entry = models.CharField(max_length=200, null=True, blank=True)
    entry_answer = models.CharField(max_length=200, null=True, blank=True)

    my_choices=(('Option1','Вариант 1'),
         ('Option2','Вариант 2'),
         ('Option3','Вариант 3'),
         ('Option4','Вариант 4'),
         ('Option5','Вариант 5'),
         ('Picture1','Рисунок 1'),
         ('Picture2','Рисунок 2'),
         ('Picture3','Рисунок 3'),
         ('Picture4','Рисунок 4'),
         ('Picture5','Рисунок 5'),
         ('Entry_answer','Вводимый ответ'))


    answer = MultiSelectField(choices=my_choices,
                                 max_choices=4,
                                 max_length=200, null=False, default=False)

    class Meta:
        verbose_name = "Вопросы"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f'{self.course} ||  {self.question}'



class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Результат"
        verbose_name_plural = "Результат"
