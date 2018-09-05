# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course_list.html", {"courses" : courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, "courses/course_detail.html", {"course" : course})
