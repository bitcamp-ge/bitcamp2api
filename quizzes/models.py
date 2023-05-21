from django.db import models
from lessons.models import Lesson

class Quiz(models.Model):
    question = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.question