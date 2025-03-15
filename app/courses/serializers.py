from rest_framework import serializers
from app.courses.models import Course  # Если courses в app


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'