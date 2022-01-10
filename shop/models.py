from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

class Item(models.Model):
	title = models.CharField(max_length=200)
	price = models.FloatField()
	description = models.TextField()
	image = models.FileField(upload_to='pictures')
	cat = models.CharField(max_length=200)

	def __str__(self):
		return self.title

class Category(models.Model):
	title = models.CharField(max_length=200)
	parent = models.CharField(max_length=200, blank=True)
	image = models.FileField(upload_to='pictures')

	def __str__(self):
		return self.title