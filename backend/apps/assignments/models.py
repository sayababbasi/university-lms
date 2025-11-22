# # # apps/assignments/models.py
# # from django.db import models
# # from apps.users.models import Student, Teacher

# # class Assignment(models.Model):
# #     title = models.CharField(max_length=255)
# #     description = models.TextField()
# #     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
# #     due_date = models.DateTimeField()

# #     def __str__(self):
# #         return self.title

# # class Submission(models.Model):
# #     assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
# #     student = models.ForeignKey(Student, on_delete=models.CASCADE)
# #     submitted_at = models.DateTimeField(auto_now_add=True)
# #     file = models.FileField(upload_to='submissions/')

# #     def __str__(self):
# #         return f"{self.student.user.username} - {self.assignment.title}"

# # class Grade(models.Model):
# #     submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
# #     grade = models.CharField(max_length=5)
# #     feedback = models.TextField(blank=True, null=True)

# #     def __str__(self):
# #         return f"{self.submission} - {self.grade}"


# # apps/assignments/models.py
# # Developed by SAYAB

# from django.db import models
# from apps.users.models import Student, Teacher
# from apps.courses.models import Course

# class Assignment(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     due_date = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

# class Submission(models.Model):
#     assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     submitted_file = models.FileField(upload_to='submissions/')
#     submitted_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.student.user.username} - {self.assignment.title}"

# class Grade(models.Model):
#     submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
#     score = models.DecimalField(max_digits=5, decimal_places=2)
#     feedback = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.submission.student.user.username} - {self.score}"

# apps/assignments/models.py
# Developed by SAYAB

from django.db import models
from apps.users.models import Student, Teacher
from apps.courses.models import Course

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="submissions/", blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.user.username}"

class Grade(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE)
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    graded_by = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.submission} - {self.marks}"
