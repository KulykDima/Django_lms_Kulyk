from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from groups.forms import CreateGroupForm, EditGroup, GroupFilterSet
from groups.models import Group

from students.models import Student


class ListGroupView(ListView):
    model = Group
    template_name = 'list_of_group.html'

    def get_queryset(self):
        groups = Group.objects.select_related('headman__group', 'course')
        filter_form = GroupFilterSet(data=self.request.GET, queryset=groups)

        return filter_form


class DetailGroupView(DetailView):
    model = Group
    template_name = 'group_detail.html'


# def detail_group(request, group_id):
#     group = get_object_or_404(Group, id=group_id)
#     return render(request=request,
#                   template_name='group_detail.html',
#                   context={
#                       'group': group
#                   })


class UpdateGroupView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = EditGroup
    success_url = reverse_lazy('group:list')
    template_name = 'edit_g.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = self.get_object().students.prefetch_related('headman_group')

        return context

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            pass
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        pk = form.cleaned_data['headman_field']
        if pk:
            form.instance.headman = Student.objects.get(pk=pk)
        else:
            form.instance.headman = None
        form.save()

        return response


class CreateGroupView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = CreateGroupForm
    success_url = reverse_lazy('group:list')
    template_name = 'create_g.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        group = form.save()
        students = form.cleaned_data['students']
        for student in students:
            student.group = group
            student.save()

        return response

# def get_context_data(self):
    #     context = super().get_context_data()
    #     context['students'] = self.get_object().students.prefetch_related('headman_group')
    #
    #     return context
    #
    # def get_initial(self):
    #     initial = super().get_initial()
    #     try:
    #         initial['headman_field'] = self.object.headman.pk
    #     except AttributeError:
    #         pass
    #     return initial
    #
    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     pk = form.cleaned_data['headman_field']
    #     if pk:
    #         form.instance.headman = Student.objects.get(pk=pk)
    #     else:
    #         form.instance.headman = None
    #     form.save()
    #
    #     return response

# def create_group(request):
#     form = None
#     if request.method == 'GET':
#         form = CreateGroupForm()
#     elif request.method == 'POST':
#         form = CreateGroupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('group:list'))
#
#     return render(request, 'create_g.html', {'form': form})


class DeleteGroupView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = 'delete_g.html'
    success_url = reverse_lazy('group:list')


# def delete_group(request, group_id):
#     group = get_object_or_404(Group, id=group_id)
#
#     if request.method == 'POST':
#         group.delete()
#         return HttpResponseRedirect(reverse('group:list'))
#
#     return render(request, 'delete_g.html', {'group': group})
