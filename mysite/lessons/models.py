from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model() 

class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='lesson'
    )

    def __str__(self):
        return self.name

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.PositiveIntegerField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time_seconds = models.PositiveIntegerField()
    is_viewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.lesson}"
