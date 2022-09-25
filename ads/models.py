from django.db import models


class Ads(models.Model):
	name = models.CharField(max_length=50)
	author = models.CharField(max_length=200)
	price = models.FloatField()
	address = models.CharField(max_length=120)
	description = models.CharField(max_length=200)
	is_published = models.BooleanField(default=None)


class Categories(models.Model):
	name = models.CharField(max_length=50)
