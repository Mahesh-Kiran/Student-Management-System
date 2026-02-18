from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'batch_no', 'first_name', 'last_name', 'email',
            'mobile', 'age', 'dob', 'course', 'cgpa',
            'college', 'fee', 'admission_date', 'address'
        ]
        labels = {
            'batch_no': 'Batch No',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'mobile': 'Phone No',
            'age': 'Age',
            'dob': 'Date of Birth',
            'course': 'Course',
            'cgpa': 'CGPA',
            'college': 'College',
            'fee': 'Fee',
            'admission_date': 'Admission Date',
            'address': 'Address',
        }
        widgets = {
            'batch_no': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'cgpa': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'max': '10'}),
            'college': forms.TextInput(attrs={'class': 'form-control'}),
            'fee': forms.NumberInput(attrs={'class': 'form-control'}),
            'admission_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }