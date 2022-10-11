from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from webargs.djangoparser import use_args
from webargs.fields import Str

from teachers.forms import CreateTeacher, EditTeacher
from teachers.models import Teacher


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False)
    },
    location='query'
)
def get_teachers(request, args):
    teachers = Teacher.objects.all()
    if len(args) != 0 and args.get('first_name') or args.get('last_name'):
        teachers = teachers.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    return render(request=request,
                  template_name='list_of_teachers.html',
                  context={
                      'teachers': teachers
                  })


def detail_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request=request,
                  template_name='detail_of_teacher.html',
                  context={
                      'teacher': teacher
                  })


def edit_teacher(request, teacher_id):
    post = get_object_or_404(Teacher, id=teacher_id)
    form = EditTeacher(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('teacher:list'))

    return render(request, 'edit_t.html', {'form': form})


def create_teacher(request):
    form = None
    if request.method == 'GET':
        form = CreateTeacher()
    elif request.method == 'POST':
        form = CreateTeacher(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teacher:list'))

    return render(request, 'create_t.html', {'form': form})


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teacher:list'))

    return render(request, 'delete_t.html', {'teacher': teacher})
