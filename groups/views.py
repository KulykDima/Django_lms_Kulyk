from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from groups.forms import CreateGroupForm, EditGroup, GroupFilterSet
from groups.models import Group


def get_groups(request):
    groups = Group.objects.all()
    filter_form = GroupFilterSet(data=request.GET, queryset=groups)
    return render(request=request,
                  template_name='list_of_group.html',
                  context={
                      'filter_form': filter_form
                  })


def detail_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    return render(request=request,
                  template_name='group_detail.html',
                  context={
                      'group': group
                  })


def edit_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = EditGroup(instance=group, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group:list'))

    form = EditGroup(instance=group)

    return render(request, 'edit_g.html', {'form': form, 'group': group})


def create_group(request):
    form = None
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group:list'))

    return render(request, 'create_g.html', {'form': form})


def delete_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('group:list'))

    return render(request, 'delete_g.html', {'group': group})
