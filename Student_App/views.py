from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from django.contrib import messages


def index(request):
    all_students = Student.objects.all()
    search_query = request.GET.get('search', '')

    if search_query:
        students = all_students.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(course__icontains=search_query)
            # NOTE: cgpa is a FloatField — icontains is not valid on floats.
            # Removed to prevent OperationalError.
        )
    else:
        students = all_students

    num_records = all_students.count()   # Always show TOTAL count in footer
    return render(request, 'Student_App/index.html', {
        'Student_App': students,
        'search_query': search_query,
        'num_records': num_records
    })


def view_student(request, id):
    # The info modal is rendered inline in index.html.
    # This URL is kept for compatibility but just redirects home.
    return HttpResponseRedirect(reverse('index'))


def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()  # Let Django handle saving all fields correctly
            student_name = f"{new_student.first_name} {new_student.last_name}"
            return render(request, 'Student_App/add.html', {
                'form': StudentForm(),
                'success': True,
                'student_name': student_name
            })
        else:
            messages.error(request, 'Invalid details. Please re-enter the information.')
            return render(request, 'Student_App/add.html', {'form': form})
    else:
        form = StudentForm()
    return render(request, 'Student_App/add.html', {'form': form})


def edit(request, id):
    student = get_object_or_404(Student, pk=id)  # Use get_object_or_404 for safety
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            updated_student = form.save()
            student_name = f"{updated_student.first_name} {updated_student.last_name}"
            return render(request, 'Student_App/edit.html', {
                'form': form,
                'success': True,
                'student_name': student_name
            })
        else:
            messages.error(request, 'Invalid details. Please correct the errors below.')
            return render(request, 'Student_App/edit.html', {'form': form})
    else:
        form = StudentForm(instance=student)
    return render(request, 'Student_App/edit.html', {'form': form})


def delete(request, id):
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))