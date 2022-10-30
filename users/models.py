from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers

from ads.models.location import Location
from datetime import date
from django.core.exceptions import ValidationError


def check_age(date_of_birth: date):
	today = date.today()
	age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
	if age < 9:
		raise ValidationError(f"Age is {age}, it may not be less than 9")


class EmailDomainValidator:
	def __init__(self, domains):
		if not isinstance(domains, list):
			domains = [domains]

		self.domains = domains

	def __call__(self, email):
		domain = email.split('@')[1]
		if domain in self.domains:
			raise serializers.ValidationError(f"Domain couldn't be {domain}")


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
	birth_date = models.DateField(null=True, validators=[check_age])
	email = models.EmailField(null=True, unique=True)

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
		ordering = ['username']

	def __str__(self):
		return self.username
