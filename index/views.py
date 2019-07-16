from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm

def index(request):
    return render(request, 'index/cs411homepage.html')


def list_students(request):
    students = Student.objects.all()
    print(students)
    return render(request, 'index/students.html', {'students': students})


def create_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_students')

    return render(request, 'index/students-form.html', {'form': form})


def update_student(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('list_students')

    return render(request, 'index/students-form.html', {'form': form, 'student': student})

def delete_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('list_students')

    return render(request, 'index/stud-delete-confirm.html', {'student': student})


