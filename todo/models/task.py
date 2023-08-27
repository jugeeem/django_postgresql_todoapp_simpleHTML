from django.db import models


class Director(models.Model):
    """Director's model"""
    title = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Task(models.Model):
    """Task's model"""
    director = models.ForeignKey(
        Director, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.title
