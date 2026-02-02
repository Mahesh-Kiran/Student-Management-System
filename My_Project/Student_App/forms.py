from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['batch_no', 'student_pin', 'first_name', 'last_name', 'email', 'mobile', 'age', 'course', 'cgpa', 'college']
    labels = {
      'batch_no' : 'Batch No',
      'student_pin': 'Student Pin',
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'email': 'Email',
      'mobile' : 'Phone No',
      'age' : 'Age',
      'course': 'Course',
      'cgpa': 'CGPA',
      'college' : 'College'
    }
    widgets = {
      'batch_no': forms.TextInput(attrs={'class': 'form-control'}),
      'student_pin': forms.NumberInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'mobile': forms.TextInput(attrs={'class': 'form-control'}),
      'age': forms.NumberInput(attrs={'class': 'form-control'}),
      'course': forms.TextInput(attrs={'class': 'form-control'}),
      'cgpa': forms.NumberInput(attrs={'class': 'form-control'}),
      'college': forms.TextInput(attrs={'class': 'form-control'})
    }
