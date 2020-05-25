from django.db import models
# import re

# class UserManager(models.Manager):
#     def register_validator(self, postdata):
#         errors = {}
#         email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         if len(postdata['pw']) < 8:
#             errors['pw'] = "Password shoudld be atleast 8 Characters"
#         if postdata['pw'] != postdata['confpw']:
#             errors['pw'] = "Passwords do no match!"
#         if len(postdata['fname']) < 2 or len(postdata['lname']) < 2:
#             errors['name'] = "Name should be longer then 2 Characters! "
#         if not email_checker.match(postdata['email']):
#             errors['email'] = "Invalid email!"
#         return errors

# class User(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     objects = UserManager()
# Create your models here.
