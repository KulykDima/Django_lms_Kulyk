from django.contrib import admin    # noqa

from groups.models import Group
from .models import Student


class GroupListFilter(admin.SimpleListFilter):
    title = 'group filter'
    parameter_name = 'group_filter'

    def lookups(self, request, model_admin):
        groups = Group.objects.all()
        lst = [(group.pk, group.group_name) for group in groups]
        lst.insert(0, (0, 'No group'))
        return tuple(lst)

    def queryset(self, request, queryset):
        match self.value():
            case None:
                return Student.objects.all()
            case '0':
                return Student.objects.filter(group__isnull=True)
            case _:
                return Student.objects.filter(group=Group.objects.get(pk=int(self.value())))


class StudentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'group_names')
    list_display_links = list_display
    list_per_page = 15
    list_filter = (GroupListFilter, )
    # fields = [
    #     ('last_name', 'first_name'),
    #     ('birthday', 'age'),
    #     'email',
    #     'phone',
    #     'group'
    # ]
    fieldsets = (
        ('Personal info', {'fields': ('last_name', 'first_name')}),
        ('Another info', {'fields': ('birthday', 'age')}),
        (None, {'fields': ('email', )}),
        (None, {'fields': ('phone', )}),
        (None, {'fields': ('group', )}),
    )

    def group_names(self, instance):
        if instance.group:
            return instance.group.group_name

        return ''

    group_names.short_description = 'Group'

    def age(self, instance):
        return f'{instance.get_age()} y.o.'

    readonly_fields = ('age', )
    age.short_description = 'age'


admin.site.register(Student, StudentAdmin)
