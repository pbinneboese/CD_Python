from __future__ import unicode_literals

from django.db import models
from ..loginReg.models import User

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=255)
	users = models.ManyToManyField(User, related_name = "courses")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
