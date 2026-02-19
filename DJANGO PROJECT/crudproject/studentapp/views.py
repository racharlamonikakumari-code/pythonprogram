from django.shortcuts import render, redirect
from .models import Student

# CREATE
def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        Student.objects.create(name=name, age=age, email=email)
        return redirect('show')
    return render(request, 'add.html')

# READ
def show_student(request):
    students = Student.objects.all()
    return render(request, 'show.html', {'students': students})

# UPDATE
def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.email = request.POST['email']
        student.save()
        return redirect('show')
    return render(request, 'update.html', {'student': student})

# DELETE
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('show')
