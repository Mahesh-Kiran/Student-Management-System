from django.db import models
from django.core.validators import RegexValidator
from django.utils.timezone import now

class Student(models.Model):
    student_pin = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    course = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    age = models.IntegerField()
    dob = models.DateField(default=now)  # Use current date as default value for dob
    batch_no = models.IntegerField(default=21124)
    college = models.CharField(max_length=100, default='T.R.R. College of Technology')
    cgpa = models.FloatField()
    fee = models.PositiveIntegerField(default=0)  # Set default value for fee to 0
    admission_date = models.DateField(default=now)  # Use current date as default value for admission_date
    address = models.TextField(default='')

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
