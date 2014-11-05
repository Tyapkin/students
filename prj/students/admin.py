from django.contrib import admin

from .models import Student, StudyGroup


class StudyGroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('group_name',)}


class StudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', 'surname')}

admin.site.register(Student, StudentAdmin)
admin.site.register(StudyGroup, StudyGroupAdmin)
