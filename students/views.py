
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    total_students = Student.objects.count()

    recent_students = Student.objects.order_by(
        '-created_at'
    )[:5]

    departments = Student.objects.values(
        'department'
    ).distinct().count()

    context = {
        'total_students': total_students,
        'recent_students': recent_students,
        'total_departments': departments,
    }

    return render(request, 'students/dashboard.html', context)

@login_required
def add_student(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Student added successfully!'
            )
            return redirect('dashboard')

    else:
        form = StudentForm()

    return render(
        request,
        'students/add_student.html',
        {'form': form}
    )
@login_required
def student_list(request):

    query = request.GET.get('search', '')

    students = Student.objects.all()

    if query:
        students = students.filter(
            full_name__icontains=query
        ) | students.filter(
            register_number__icontains=query
        )

    context = {
        'students': students,
        'query': query,
    }

    return render(
        request,
        'students/student_list.html',
        context
    )    

@login_required    
def edit_student(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Student updated successfully!'
            )
            return redirect('dashboard')

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        'students/edit_student.html',
        {
            'form': form,
            'student': student,
        }
    )    

@login_required    
def delete_student(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()

        messages.success(
            request,
            'Student deleted successfully!'
        )

        return redirect('dashboard')

    return render(
        request,
        'students/delete_student.html',
        {'student': student}
    )    