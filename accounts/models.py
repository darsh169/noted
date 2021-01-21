from django.db import models
from django.contrib.auth.models import User,auth

# Create your models here.
class Notes(models.Model):
	content=models.TextField(max_length=1000)
	title=models.CharField(max_length=100)
	user_id=models.ForeignKey(User,on_delete=models.CASCADE)