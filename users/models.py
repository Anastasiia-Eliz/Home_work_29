from django.db import models
from django.contrib.auth.models import AbstractUser
from ads.models.location import Location

class User(AbstractUser):
    ADMIN = 'admin'
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ROLES = [
        (ADMIN, 'администратор'),
        (MEMBER, 'пользователь'),
        (MODERATOR, 'модератор')
    ]

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)
    role = models.CharField(max_length=10, choices=ROLES, default='member', null=True)
    age = models.SmallIntegerField(null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username