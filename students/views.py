from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CreateStudentForm, EditStudentForm, StudentFilterForm
from .models import Student


# # @use_args(
# #     {
# #         'first_name': Str(required=False),
# #         'last_name': Str(required=False),
# #     },
# #     location='query'
# #  )
# def get_students(request):
#     students = Student.objects.select_related('group', 'headman_group')
#
#     filter_form = StudentFilterForm(data=request.GET, queryset=students)
#     # if len(args) != 0 and args.get('first_name') or args.get('last_name'):
#     #     students = students.filter(
#     #         Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
#     #         )
#     # if 'first_name' in args:
#     #     students = students.filter(first_name=args['first_name'])
#     #
#     # if 'last_name' in args:
#     #     students = students.filter(last_name=args['last_name'])
#
#     # html_form = '''
#     #
#     #     '''
#     #
#     # html = qs2html(students)
#
#     # response = HttpResponse(html_form + html)
#     # return response
#     return render(request=request,
#                   template_name='students/list.html',
#                   context={
#                       # 'title': 'List of students',
#                       # 'students': students,
#                       'filter_form': filter_form
#                   })


class ListStudentsView(ListView):
    model = Student
    template_name = 'students/list.html'

    def get_queryset(self):
        students = Student.objects.select_related('group', 'headman_group')
        filter_form = StudentFilterForm(data=self.request.GET, queryset=students)

        return filter_form


class DetailStudentView(DetailView):
    model = Student
    template_name = 'students/details.html'


# def detail_student(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     return render(request=request,
#                   template_name='students/details.html',
#                   context={
#                       'title': 'Student',
#                       'student': student
#                   })


# def create_student(request):
#     # CreateStudentForm
#     form = None
#     if request.method == 'GET':
#         form = CreateStudentForm()
#     elif request.method == 'POST':
#         form = CreateStudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('student:list'))
#
#     return render(request, 'students/create.html', {'form': form})


class CreateStudentView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = CreateStudentForm
    success_url = reverse_lazy('student:list')
    template_name = 'students/create.html'


class UpdateStudentView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = EditStudentForm
    success_url = reverse_lazy('student:list')
    template_name = 'students/edit.html'


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = 'delete_g.html'
    success_url = reverse_lazy('student:list')

# def delete_student(request, student_id):
#     student = Student.objects.get(id=student_id)
#
#     if request.method == 'POST':
#         student.delete()
#         return HttpResponseRedirect(reverse('student:list'))
#
#     return render(request, 'students/delete.html', {'student': student})
