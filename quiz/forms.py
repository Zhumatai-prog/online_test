from django import forms
from django.contrib.auth.models import User
from . import models


class CourseForm(forms.ModelForm):
    class Meta:
        model=models.Course
        fields=['course_name', 'dept', 'position']

class QuestionForm(forms.ModelForm):

    #this will show dropdown __str__ method course model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in course model and return it
    courseID=forms.ModelChoiceField(queryset=models.Course.objects.all(),empty_label="Course Name", to_field_name="id")
    class Meta:
        model=models.Question
        fields=['question','option1','option2','option3','option4','option5',
                'picture1','picture2','picture3','picture4','picture5', 'entry_answer','answer']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 3, 'cols': 50})
        }
