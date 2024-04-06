from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    complated = models.BooleanField(default=False, verbose_name='Завершено')
    created = models.DateTimeField(auto_now_add=True)
