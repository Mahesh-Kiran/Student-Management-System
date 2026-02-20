from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import hashlib
import json
import uuid

def index(request):
    all_students = Student.objects.all()
    search_query = request.GET.get('search', '')

    if search_query:
        students = all_students.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(course__icontains=search_query)
        )
        num_records = students.count()
    else:
        students = all_students
        num_records = all_students.count()

    paginator = Paginator(students, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    student_data = list(all_students.values('student_pin', 'first_name', 'last_name', 'cgpa'))
    etag_value = f'"{hashlib.md5(json.dumps(student_data, default=str).encode()).hexdigest()}"'

    if request.META.get('HTTP_IF_NONE_MATCH') == etag_value:
        return HttpResponse(status=304)

    response = render(request, 'Student_App/index.html', {
        'page_obj': page_obj,           
        'search_query': search_query,
        'num_records': num_records
    })
    response['ETag'] = etag_value
    return response

def add(request):
    if request.method == 'GET':
        form = StudentForm()
        idempotency_key = str(uuid.uuid4())
        request.session['idempotency_key'] = idempotency_key
        return render(request, 'Student_App/add.html', {
            'form': form,
            'idempotency_key': idempotency_key
        })

    if request.method == 'POST':
        submitted_key = request.POST.get('idempotency_key')
        session_key = request.session.get('idempotency_key')

        if not submitted_key or submitted_key != session_key:
            messages.error(request, 'Duplicate submission detected. Please try again.')
            return HttpResponseRedirect(reverse('add'))

        del request.session['idempotency_key']

        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            student_name = f"{new_student.first_name} {new_student.last_name}"
            new_key = str(uuid.uuid4())
            request.session['idempotency_key'] = new_key
            return render(request, 'Student_App/add.html', {
                'form': StudentForm(),
                'success': True,
                'student_name': student_name,
                'idempotency_key': new_key
            })
        else:
            new_key = str(uuid.uuid4())
            request.session['idempotency_key'] = new_key
            messages.error(request, 'Invalid details. Please re-enter the information.')
            return render(request, 'Student_App/add.html', {
                'form': form,
                'idempotency_key': new_key
            })

def edit(request, id):
    student = get_object_or_404(Student, pk=id)
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


@csrf_exempt
def api_add_student(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

   
    idempotency_key = request.headers.get('Idempotency-Key')
    if not idempotency_key:
        return JsonResponse({'error': 'Idempotency-Key header is required'}, status=400)

    cache_key = f"idem_{idempotency_key}"
    existing = request.session.get(cache_key)
    if existing:
        return JsonResponse({
            'message': 'Already processed — duplicate request ignored',
            'student': existing
        }, status=200)

    form = StudentForm(data)
    if form.is_valid():
        student = form.save()
        response_data = {
            'student_pin': student.student_pin,
            'name': f"{student.first_name} {student.last_name}",
            'email': student.email,
            'course': student.course
        }
        request.session[cache_key] = response_data
        return JsonResponse({'message': 'Student created', 'student': response_data}, status=201)
    else:
        return JsonResponse({'errors': form.errors}, status=400)