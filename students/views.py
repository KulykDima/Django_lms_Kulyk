from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render         # noqa

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateStudentForm, EditStudentForm
from .forms import CreateStudentForm
from .models import Student
from .utils import qs2html


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

    html_form = '''
            <form method="get">
                <label for="first_name">First name:</label><br>
                <input type="text" id="first_name" name="first_name" placeholder="John"><br>
                <label for="last_name">Last name:</label><br>
                <input type="text" id="last_name" name="last_name" placeholder="Doe"><br><br>
                <input type="submit" value="Submit">
                </form> 
            '''
    # if 'first_name' in args:
    #     students = students.filter(first_name=args['first_name'])
    #
    # if 'last_name' in args:
    #     students = students.filter(last_name=args['last_name'])

    html_form = '''
        <form method="get">
            <label for="first_name">First name:</label><br>
            <input type="text" id="first_name" name="first_name" placeholder="John"><br>
            <label for="last_name">Last name:</label><br>
            <input type="text" id="last_name" name="last_name" placeholder="Doe"><br><br>
            <input type="submit" value="Submit">
            </form> 
        '''

    html = qs2html(students)

    response = HttpResponse(html_form + html)
    return response


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
            </form> 
            '''
    return HttpResponse(html_form)
