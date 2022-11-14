from django.contrib import admin    # noqa
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from Courses.models import Course
from groups.models import Group


class StudentInlineTable(admin.TabularInline):
    from students.models import Student
    model = Student
    fields = ('first_name', 'last_name')
    extra = 0
    readonly_fields = fields
    # show_change_link = True

    def get_queryset(self, request):
        queryset = self.model.objects.filter(
            group_id=int(request.resolver_match.kwargs['object_id'])
        ).select_related('group')

        return queryset

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


class TeachersInlineTable(admin.TabularInline):
    model = Group.teachers.through
    fields = ('teacher_name', 'teacher_lastname')
    readonly_fields = fields

    def teacher_name(self, obj):
        return obj.teacher.first_name

    def teacher_lastname(self, obj):
        return obj.teacher.last_name

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return True


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


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'date_of_start', 'headman', 'count')
    list_display_links = list_display
    list_per_page = 15
    list_filter = (GroupListFilter, )
    # fields = ('group_name', ('date_of_start, 'end_date'), 'teachers', 'headman')
    fieldsets = (
        ('Main info', {'fields': ('group_name', 'date_of_start', 'group_description')}),
        ('Courses', {'fields': ('course', 'headman', )}),
        (None, {'fields': ('end_date',)}),
    )

    def count(self, obj):
        count = obj.students.count()
        url = (
            reverse("admin:students_student_changelist") + '?' + urlencode({'group_id': f'{obj.pk}'})
        )   # group_id = pk&...

        return format_html('<a href="{}">{} student(s)</a>', url, count)

    # def count(self, instance):
    #     if instance.students:
    #         return instance.students.count()

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        form.base_fields['headman'].widget.can_change_related = False
        form.base_fields['headman'].widget.can_delete_related = False
        form.base_fields['headman'].widget.can_view_related = False
        form.base_fields['headman'].queryset = obj.students.all()

        return form

    inlines = [StudentInlineTable, TeachersInlineTable, ]
