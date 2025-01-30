from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView 
from django.urls import reverse_lazy
from .models import LearningCourse

class CourseList(ListView):
    model=LearningCourse
    template_name='employee_training/course_list.html'
    context_object_name='course_object_list'

class CourseDetail(DetailView):
    model=LearningCourse
    template_name='employee_training/course_detail.html'
    context_object_name='course_object'

class CourseCreate(CreateView):
    model=LearningCourse
    template_name='employee_training/course_create.html'
    fields=('title','level','employee')
    success_url=reverse_lazy('course_list')

class CourseUpdate(UpdateView):
    model=LearningCourse
    template_name='employee_training/course_update.html'
    fields=('title','level','employee')
    success_url=reverse_lazy('course_list')

class CourseDelete(DeleteView):
    model=LearningCourse
    template_name='employee_training/course_delete.html'
    success_url=reverse_lazy('course_list')

class Index(TemplateView):
    template_name='index.html'
