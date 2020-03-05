from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

"""Sign up table """

class Signup(models.Model):
	user_id = models.OneToOneField(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.user_id.username 