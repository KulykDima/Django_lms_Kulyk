from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateStudentForm, EditStudentForm
from .models import Student
# from .utils import qs2html


def index(request):
    return HttpResponse('Welcome to LMS')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query'
 )
def get_students(request, args):
    students = Student.objects.all()

    if len(args) != 0 and args.get('first_name') or args.get('last_name'):
        students = students.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

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
                      'title': 'List of students',
                      'students': students
                  })


def detail_student(request, student_id):
    student = Student.objects.get(pk=student_id)
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
            return HttpResponseRedirect('/students/')

    token = get_token(request)
    html_form = f'''
                <form method="post">
                    <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
                    <table>
                        {form.as_table()}
                    </table>
                    <input type="submit" value="Submit">
                </form> 
                '''

    return HttpResponse(html_form)


def edit_student(request, student_id):
    # EditStudentForm
    post = Student.objects.get(id=student_id)
    form = EditStudentForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/students/')

    token = get_token(request)
    html = f'''
            <form method="post">
            <h1>Update Student</h1>
            <h2>{post.first_name} {post.last_name}</h2>
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
            <form method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
                <table>
                    {form.as_table()}
                </table>
                <input type="submit" value="Submit">
            </form>
    '''
    return HttpResponse(html)
