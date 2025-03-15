from django.shortcuts import render
from app.courses.models import Course
from app.API.serializers.courses_serializers import CourseSerializer
from rest_framework import generics


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer 