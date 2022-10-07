from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from groups.forms import CreateGroupForm, EditGroup
from groups.models import Group

from webargs.djangoparser import use_args
from webargs.fields import Str


@use_args(
    {
        'group_name': Str(required=False)
    },
    location='query'
)
def get_groups(request, args):
    groups = Group.objects.all()
    if len(args) != 0 and args.get('group_name'):
        groups = groups.filter(
            Q(group_name=args.get('group_name'))
        )
    return render(request=request,
                  template_name='list_of_group.html',
                  context={
                      'groups': groups
                  })


def detail_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    return render(request=request,
                  template_name='group_detail.html',
                  context={
                      'group': group
                  })


def edit_group(request, group_id):
    post = get_object_or_404(Group, id=group_id)
    form = EditGroup(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('group:list'))

    return render(request, 'edit_g.html', {'form': form})


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
