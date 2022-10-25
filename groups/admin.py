from django.contrib import admin    # noqa

from Courses.models import Course
from groups.models import Group
from students.models import Student


class GroupListFilter(admin.SimpleListFilter):
    title = 'Course filter'
    parameter_name = 'course_filter'

    def lookups(self, request, model_admin):
        courses = Course.objects.all()
        lst = [(course.pk, course.title) for course in courses]
        lst.insert(0, (0, 'No Course'))
        return tuple(lst)

    def queryset(self, request, queryset):
        match self.value():
            case None:
                return Group.objects.all()
            case '0':
                return Group.objects.filter(course__isnull=True)
            case _:
                return Group.objects.filter(course=Course.objects.get(pk=int(self.value())))


class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'date_of_start', 'headman', 'course')
    list_display_links = list_display
    list_per_page = 15
    list_filter = (GroupListFilter, )

    fieldsets = (
        ('Main info', {'fields': ('group_name', 'date_of_start', 'group_description')}),
        ('Courses', {'fields': ('course', 'headman', 'teachers')}),
        (None, {'fields': ('end_date',)}),
    )


admin.site.register(Group, GroupAdmin)
