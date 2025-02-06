from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True)
    nickname = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'Nickname: {self.nickname} | Email: {self.email}'

class Task(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')