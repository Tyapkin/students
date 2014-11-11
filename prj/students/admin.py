from django.contrib import admin

from .models import Student, StudyGroup


class StudyGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('group_name',)}


class StudentAdmin(admin.ModelAdmin):
    fields = (
        ('name', 'surname', 'patronymic'), 'slug',
        'bdate', 'email', 'student_card', 'group')
    list_display = ('get_full_name', 'student_card', 'group')
    prepopulated_fields = {'slug': ('name', 'surname')}

admin.site.register(Student, StudentAdmin)
admin.site.register(StudyGroup, StudyGroupAdmin)
