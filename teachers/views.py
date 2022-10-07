from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render

from teachers.forms import EditTeacher
from teachers.models import Teacher


def get_teachers(request):
    teachers = Teacher.objects.all()
    return render(request=request,
                  template_name='list_of_teachers.html',
                  context={
                      'teachers': teachers
                  })


def detail_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return render(request=request,
                  template_name='detail_of_teacher.html',
                  context={
                      'teacher': teacher
                  })


def edit_teacher(request, teacher_id):
    post = Teacher.objects.get(pk=teacher_id)
    form = EditTeacher(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/teachers/')

    token = get_token(request)
    html = f'''
                    <form method="post">
                    <h1>Edit Teacher</h1>
                    <h2>{post.first_name}</h2>
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
