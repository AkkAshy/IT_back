from django.db import models
from app.courses.models import Course

class UserProfile(models.Model):

    STATUS_CHOICES = (
        ('old', 'Старый'),
        ('new', 'Новый'),
    )

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    registered_at = models.DateTimeField(auto_now_add=True)
    contacted = models.CharField(max_length=3, choices=STATUS_CHOICES, default='new')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="students")  # Связь с курсом


    def __str__(self):
        return f"{self.name} {self.phone} - {self.get_contacted_display()}"
    
    class Meta:
        app_label = 'Users'
    


