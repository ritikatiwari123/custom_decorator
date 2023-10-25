from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Example(User):
    example_data = models.CharField(max_length=25)

    class Meta:
        db_table = 'example'


class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()

    class Meta:
        db_table = 'student'


class Teacher(models.Model):
    subject = models.CharField(max_length=50)
    student = models.ForeignKey(Student)

    class Meta:
        db_table = 'teacher'

# class UserAccountManager(BaseUserManager):
#
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("Email is required to create user")
#         if not username:
#             raise ValueError("User name is required to create user")
#         if not password:
#             raise ValueError("Password is required to create password")
#
#         user = self.model(email=email, username=username)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, username, password=None):
#         user = self.create_user(email, username, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.is_admin = True
#         user.save()
#         return user
#
#     def create_student(self, email, username, password):
#         user = self.create_user(email, username, password)
#         user.is_student = True
#         user.save()
#         return user
#
#     def create_principal(self, email, username, password):
#         user = self.create_user(email, username, password)
#         user.is_principal = True
#         user.save()
#         return user
#
#     def create_teacher(self, email, username, password):
#         user = self.create_user(email, username, password)
#         user.is_teacher = True
#         user.save()
#         return user
#
#
# class CustomUser(TimeStampModel):
#     email = models.CharField(max_length=25)
#     user_name = models.CharField(max_length=25)
#     password = models.CharField(max_length=25)
#
#
#     class Meta:
#         db_table = 'user'






