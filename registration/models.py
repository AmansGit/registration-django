from django.db import models

from django.utils.crypto import get_random_string
# Create your models here.


def user_image(instance, filename):
	return 'user_{0}/{1}'.format(instance, filename)

class User_registration(models.Model):
	image		= models.ImageField(upload_to=user_image)
	first_name 	= models.CharField(max_length=20, null=True, blank=True)
	last_name 	= models.CharField(max_length=20, null=True, blank=True)
	age 		= models.IntegerField(null=True, blank=True)
	unique_id 	= get_random_string(length=8)											# models.AutoField( default=True)
	email_id	= models.EmailField(max_length=200, null=True, blank=True)
	password 	= models.CharField(max_length=50,blank=False)

	class Meta:
		db_table = "user"

	def __str__(self):
		return self.username


