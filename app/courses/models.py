from django.db import models

class Course(models.Model): 
    COURSE_TYPE = (
        ('online', 'Онлайн'),
        ('offline', 'Оффлайн'),
    )

    SERTIFICATE_OPTIONS = (
        ('yes', 'Да'),
        ('no', 'Нет'),
    )

    title = models.CharField(max_length=100, verbose_name= "Название курса") # Название курса
    teacher = models.CharField(max_length=100, verbose_name='Преподаватель') #  Преподаватель
    prise = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена') # Цена
    duration = models.CharField(max_length=100, verbose_name='Продолжительность') # Продолжительность
    course_type = models.CharField(max_length=100, choices=COURSE_TYPE, verbose_name='Формат обучения') # Формат обучения
    description = models.TextField(verbose_name='Описание курса')   # Описание
    certificate = models.CharField(max_length=100, choices=SERTIFICATE_OPTIONS, verbose_name='Сертификат') # Сертификат


    def __str__(self): # Вывод названия курса в админке
        return self.title # Вывод названия курса в админке
# Compare this snippet from app/courses/views.py:
