from django.shortcuts import render, HttpResponse

from .models import Student


def index(request):
    message = 'Let\'s Learn dJango..!!'
    context = {'message': message}
    return render(request, 'student/index.html', context)


def details(request):
    students = Student.objects.all()
    return render(request, 'student/details.html', {'students': students})


def info(request, student_id):
    student = Student.objects.get(pk=student_id)
    sports = student.sports_set.all()
    return render(request, 'student/info.html', {'student': student, 'sports':sports})
