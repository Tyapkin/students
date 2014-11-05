# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import auth
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.forms import DateInput

from .models import StudyGroup, Student


class IndexView(RedirectView):

    query_string = True
    pattern_name = 'group_list'


class GroupList(TemplateView):
    model = StudyGroup
    template_name = 'students/group_list.html'

    def get_context_data(self, **kwargs):
        context = super(GroupList, self).get_context_data(**kwargs)
        context['group_list'] = self.model.objects.all()
        context['count'] = {}

        for i in context['group_list']:
            obj = get_list_or_404(Student, group=i.id)
            context['count'][i.id] = len(obj)

        return context


class Group(TemplateView):
    model = StudyGroup
    template_name = 'students/group_detail.html'

    def get(self, request, **kwargs):
        group = get_object_or_404(self.model, id=self.kwargs['pk'])
        students = get_list_or_404(Student, group=group.id)
        return render(request, self.template_name, {
            'group': group,
            'students': students})


class StudentDetail(DetailView):
    model = Student
    template_name = 'students/student_detail.html'


class AddStudent(CreateView):
    model = Student
    fields = [
        'name', 'surname', 'patronymic', 'email',
        'bdate', 'student_card', 'group']
    widgets = {
        'bdate': DateInput(),
    }


class EditStudent(UpdateView):
    model = Student
    fields = [
        'name', 'surname', 'patronymic', 'email',
        'bdate', 'student_card', 'group']


class DeleteStudent(DeleteView):
    model = Student
    success_url = reverse_lazy('group_list')


def logout(request):
    from django.contrib.auth import logout

    logout(request)
    redirect_to = request.REQUEST.get(
        auth.REDIRECT_FIELD_NAME, settings.LOGOUT_REDIRECT_URL)

    return redirect(redirect_to)
