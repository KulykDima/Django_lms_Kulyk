from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from teachers.forms import CreateTeacher, EditTeacher, TeacherFilterForm
from teachers.models import Teacher


class ListTeacherView(ListView):
    model = Teacher
    template_name = 'list_of_teachers.html'
    # context_object_name = 'posts'
    # paginate_by = 50

    def get_queryset(self):
        teacher = Teacher.objects.all()
        filter_form = TeacherFilterForm(data=self.request.GET, queryset=teacher)

        return filter_form


class DetailTeacherView(DetailView):
    model = Teacher
    template_name = 'detail_of_teacher.html'


class UpdateTeacherView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = EditTeacher
    success_url = reverse_lazy('teacher:list')
    template_name = 'edit_t.html'


class CreateTeacherView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = CreateTeacher
    success_url = reverse_lazy('teacher:list')
    template_name = 'create_t.html'


class DeleteTeacherView(LoginRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'delete_t.html'
    success_url = reverse_lazy('teacher:list')


# def get_teachers(request,):
#     teachers = Teacher.objects.all()
#     filter_form = TeacherFilterForm(data=request.GET, queryset=teachers)
#
#     return render(request=request,
#                   template_name='list_of_teachers.html',
#                   context={
#                       'filter_form': filter_form
#                   })


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


# def delete_teacher(request, teacher_id):
#     teacher = get_object_or_404(Teacher, id=teacher_id)
#
#     if request.method == 'POST':
#         teacher.delete()
#         return HttpResponseRedirect(reverse('teacher:list'))
#
#     return render(request, 'delete_t.html', {'teacher': teacher})
