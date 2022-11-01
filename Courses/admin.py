from django.contrib import admin    # noqa

from Courses.models import Course
from groups.models import Group


class CourseListFilter(admin.SimpleListFilter):
    title = 'Group filter'
    parameter_name = 'course_filter'

    def lookups(self, request, model_admin):
        groups = Group.objects.all()
        li = [(group.pk, group.group_name) for group in groups]
        li.insert(0, (0, 'No groups'))
        return tuple(li)

    def queryset(self, request, queryset):
        match self.value():
            case None:
                return Course.objects.all()
            case '0':
                return Course.objects.filter(course_group__isnull=True)
            case _:
                return Course.objects.filter(course_group=Group.objects.get(pk=self.value()))


class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'price', 'lessons', 'group_names')
    list_display_links = list_display
    list_per_page = 5
    list_filter = (CourseListFilter, 'price', )
    fieldsets = (
        ('Main info', {'fields': ('title', 'price', 'lessons')}),
    )

    def group_names(self, instance):
        if instance.course_group:
            return instance.course_group.group_name

        return ''


admin.site.register(Course, AdminCourse)
