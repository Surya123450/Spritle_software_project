from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Master, Student

class MasterForm(UserCreationForm):
    class Meta:
        model = Master
        fields = ['username', 'email']

class StudentForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['username', 'email']
