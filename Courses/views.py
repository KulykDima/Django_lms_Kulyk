from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from Courses.forms import EditCourse, CreateCourseForm
from Courses.models import Course
from Courses.forms import GroupFilterSet


def get_course(request):
    courses = Course.objects.all()
    filter_form = GroupFilterSet(data=request.GET, queryset=courses)
    return render(request=request,
                  template_name='list_c.html',
                  context={
                      'filter_form': filter_form
                  })


def detail_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request=request,
                  template_name='detail.html',
                  context={
                      'course': course
                  })


def edit_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = EditCourse(instance=course, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('course:list'))

    form = EditCourse(instance=course)

    return render(request, 'update.html', {'form': form, 'course': course})


def create_course(request):
    form = None
    if request.method == 'GET':
        form = CreateCourseForm()
    elif request.method == 'POST':
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('course:list'))

    return render(request, 'create.html', {'form': form})


def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.delete()
        return HttpResponseRedirect(reverse('course:list'))

    return render(request, 'delete.html', {'course': course})
