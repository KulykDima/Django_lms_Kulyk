from django.db.models import Q      # noqa
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .forms import CreateStudentForm, EditStudentForm, StudentFilterForm
from .models import Student


# @use_args(
#     {
#         'first_name': Str(required=False),
#         'last_name': Str(required=False),
#     },
#     location='query'
#  )
def get_students(request):
    students = Student.objects.all()

    filter_form = StudentFilterForm(data=request.GET, queryset=students)
    # if len(args) != 0 and args.get('first_name') or args.get('last_name'):
    #     students = students.filter(
    #         Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
    #         )
    # if 'first_name' in args:
    #     students = students.filter(first_name=args['first_name'])
    #
    # if 'last_name' in args:
    #     students = students.filter(last_name=args['last_name'])

    # html_form = '''
    #
    #     '''
    #
    # html = qs2html(students)

    # response = HttpResponse(html_form + html)
    # return response
    return render(request=request,
                  template_name='students/list.html',
                  context={
                      # 'title': 'List of students',
                      # 'students': students,
                      'filter_form': filter_form
                  })


def detail_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request=request,
                  template_name='students/details.html',
                  context={
                      'title': 'Student',
                      'student': student
                  })


def create_student(request):
    # CreateStudentForm
    form = None
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('student:list'))

    return render(request, 'students/create.html', {'form': form})


def edit_student(request, student_id):
    # EditStudentForm
    post = get_object_or_404(Student, id=student_id)
    form = EditStudentForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('student:list'))

    return render(request, 'students/edit.html', {'form': form})


def delete_student(request, student_id):
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('student:list'))

    return render(request, 'students/delete.html', {'student': student})
