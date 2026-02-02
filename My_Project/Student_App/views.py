from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from django.contrib import messages
def index(request):
    students = Student.objects.all()
    search_query = request.GET.get('search', '')

    if search_query:
        students = students.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(course__icontains=search_query) |
            Q(cgpa__icontains=search_query)
        )
    num_records = students.count()
    return render(request, 'Student_App/index.html', {'Student_App': students, 'search_query': search_query, 'num_records': num_records})

def view_student(request, id):
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_batch_no = form.cleaned_data['batch_no']
            new_student_pin = form.cleaned_data['student_pin']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_mobile = form.cleaned_data['mobile']
            new_age = form.cleaned_data['age']
            new_course = form.cleaned_data['course']
            new_cgpa = form.cleaned_data['cgpa']
            new_college = form.cleaned_data['college']

            new_student = Student(
                batch_no=new_batch_no,
                student_pin=new_student_pin,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                mobile=new_mobile,
                age=new_age,
                course=new_course,
                cgpa=new_cgpa,
                college=new_college
            )
            new_student.save()
            student_name = f"{new_student.first_name} {new_student.last_name}"
            return render(request,'Student_App/add.html', {
                'form' : StudentForm(),
                'success' : True,
                'show_search_form': True,
                'student_name': student_name
            })
        else:
            messages.error(request, 'Invalid credentials Re-enter the details.')
    else:
        form = StudentForm()
    return render (request, 'Student_App/add.html', {
        'form' : StudentForm(),
        'show_search_form': True
    })

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            updated_student_name =  f"{student.first_name} {student.last_name}"
            return render(request, 'Student_App/edit.html',{
                'form': form,
                'success': True,
                'student_name': updated_student_name,
                'show_search_form': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'Student_App/edit.html', {
        'form': form,
        'show_search_form': True
    })

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
