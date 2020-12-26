from django.contrib.auth.decorators import login_required
from academics.models import Class, Note, Subject
from users.models import StudentProfile, Teach, TeacherProfile
from django.shortcuts import render, redirect, get_object_or_404
from academics.forms import AddNotesForm
from django.contrib import messages
from djangoProject.utils import is_student, is_teacher


# get list of classes for teacher get list of subjects for student  -- notes section
@login_required
def view_list(request):
    if is_student(request):
        student_profile = get_object_or_404(StudentProfile, user=request.user)
        subjects = Teach.objects.filter(Class=student_profile.section)
        return render(request, 'academics/notes-list.html', {'subjects': subjects})
    elif is_teacher(request):
        teaches = Teach.objects.filter(teacher__user=request.user)
        return render(request, 'academics/notes-list.html', {'teaches': teaches})


# view notes for student, add and view notes for teacher
@login_required
def view_notes(request, subjectId):
    notes = Note.objects.filter(subject=subjectId)
    if is_teacher(request):
        if request.method == 'GET':
            form = AddNotesForm()
            return render(request, 'academics/notes-detail.html', {'notes': notes, 'form': form})
        elif request.method == 'POST':
            form = AddNotesForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                subject = Subject.objects.get(id=subjectId)
                note.subject = subject
                teacherProfile = TeacherProfile(user=request.user)
                note.department = teacherProfile.department
                form.save()
                messages.success(request,
                                 message="Notes added successfully")
            return render(request, 'academics/notes-detail.html', {'notes': notes, 'form': form}, )
    elif is_student(request):
        notes = Note.objects.filter(subject=subjectId)
        return render(request, 'academics/notes-detail.html', {'notes': notes})


# view list of class for teacher , get details of his class student -- class
@login_required
def class_list(request):
    if is_student(request):
        student_profile = get_object_or_404(StudentProfile, user=request.user)
        class_id = student_profile.section.id
        return redirect('view-class', classId=class_id)
    else:
        teaches = Teach.objects.filter(teacher__user=request.user)
        return render(request, 'academics/class-list.html', {'teaches': teaches})


# view details of a class student and teacher
@login_required
def view_class(request, classId):
    class_obj = Class.objects.get(id=classId)
    return render(request, 'academics/class-detail.html', {'class': class_obj})
