from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    deadline = models.CharField('Дэдлайн', max_length=100)

    def __str__(self):
        return self.title
