from django.contrib import admin        # noqa

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'salary')
    list_display_links = list_display
    list_per_page = 5
    list_filter = ('salary', )

    fieldsets = (
        ('Personal info', {'fields': ('last_name', 'first_name')}),
        ('Another info', {'fields': ('phone', 'salary')}),
    )


admin.site.register(Teacher, TeacherAdmin)
