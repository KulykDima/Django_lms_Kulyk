from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render

from groups.forms import EditGroup
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
    group = Group.objects.get(pk=group_id)
    return render(request=request,
                  template_name='group_detail.html',
                  context={
                      'group': group
                  })


def edit_group(request, group_id):
    post = Group.objects.get(pk=group_id)
    form = EditGroup(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/groups/')

    token = get_token(request)
    html = f'''
                <form method="post">
                <h1>Edit Group</h1>
                <h2>{post.group_name}</h2>
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
