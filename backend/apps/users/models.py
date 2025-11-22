# # # # from django.contrib.auth.models import AbstractUser
# # # # from django.db import models

# # # # class User(AbstractUser):
# # # #     ROLE_CHOICES = (
# # # #         ('admin','Admin'),
# # # #         ('teacher','Teacher'),
# # # #         ('student','Student'),
# # # #         ('staff','Staff'),
# # # #     )
# # # #     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')


# # # from django.contrib.auth.models import AbstractUser, Group, Permission
# # # from django.db import models

# # # # --- Developed by SAYAB ---
# # # class User(AbstractUser):
# # #     # Add any custom fields here, for example:
# # #     # phone = models.CharField(max_length=20, blank=True, null=True)

# # #     groups = models.ManyToManyField(
# # #         Group,
# # #         related_name="custom_user_groups",  # <-- change this to avoid conflict
# # #         blank=True,
# # #         help_text="The groups this user belongs to.",
# # #         verbose_name="groups",
# # #     )
# # #     user_permissions = models.ManyToManyField(
# # #         Permission,
# # #         related_name="custom_user_permissions",  # <-- change this to avoid conflict
# # #         blank=True,
# # #         help_text="Specific permissions for this user.",
# # #         verbose_name="user permissions",
# # #     )


# # # apps/users/models.py
# # # Developed by SAYAB

# # from django.contrib.auth.models import AbstractUser
# # from django.db import models

# # class User(AbstractUser):
# #     # Extend with extra fields if needed
# #     is_student = models.BooleanField(default=False)
# #     is_teacher = models.BooleanField(default=False)
# #     is_staff_member = models.BooleanField(default=False)

# # class Student(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     roll_number = models.CharField(max_length=20)
# #     course = models.CharField(max_length=100)

# #     def __str__(self):
# #         return f"{self.user.username} - {self.roll_number}"

# # class Teacher(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     department = models.CharField(max_length=100)

# #     def __str__(self):
# #         return self.user.username

# # class Staff(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     role = models.CharField(max_length=100)

# #     def __str__(self):
# #         return self.user.username


# # apps/users/models.py
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# # --- Custom User Model ---
# class User(AbstractUser):
#     # Additional fields if needed
#     is_student = models.BooleanField(default=False)
#     is_teacher = models.BooleanField(default=False)
#     is_staff_member = models.BooleanField(default=False)

#     def __str__(self):
#         return self.username

# # --- Student Profile ---
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     enrollment_number = models.CharField(max_length=50)
#     course = models.CharField(max_length=100)

#     def __str__(self):
#         return self.user.username

# # --- Teacher Profile ---
# class Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     department = models.CharField(max_length=100)

#     def __str__(self):
#         return self.user.username

# # --- Staff Profile ---
# class Staff(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=100)

#     def __str__(self):
#         return self.user.username


# apps/users/models.py
# Developed by SAYAB

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
