# # # apps/results/models.py
# # # Developed by SAYAB

# # from django.db import models
# # from apps.users.models import Student
# # from apps.courses.models import Course

# # class Result(models.Model):
# #     student = models.ForeignKey(Student, on_delete=models.CASCADE)
# #     course = models.ForeignKey(Course, on_delete=models.CASCADE)
# #     marks_obtained = models.FloatField()
# #     total_marks = models.FloatField()
# #     date_recorded = models.DateField(auto_now_add=True)

# #     def __str__(self):
# #         return f"{self.student.user.username} - {self.course.title}"

# # class Transcript(models.Model):
# #     student = models.ForeignKey(Student, on_delete=models.CASCADE)
# #     gpa = models.FloatField()
# #     created_at = models.DateField(auto_now_add=True)

# #     def __str__(self):
# #         return f"{self.student.user.username} Transcript"

# # class GPA(models.Model):
# #     student = models.ForeignKey(Student, on_delete=models.CASCADE)
# #     semester = models.IntegerField()
# #     gpa_value = models.FloatField()

# #     def __str__(self):
# #         return f"{self.student.user.username} - Semester {self.semester}"


# # apps/results/models.py
# # Developed by SAYAB

# from django.db import models
# from apps.users.models import Student

# class Result(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     exam_name = models.CharField(max_length=200)
#     score = models.DecimalField(max_digits=5, decimal_places=2)
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.student.user.username} - {self.exam_name}"

# class Transcript(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     gpa = models.DecimalField(max_digits=4, decimal_places=2)
#     issued_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.student.user.username} - GPA: {self.gpa}"

# class GPA(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     semester = models.PositiveIntegerField()
#     gpa = models.DecimalField(max_digits=4, decimal_places=2)

#     def __str__(self):
#         return f"{self.student.user.username} - Sem {self.semester} - GPA {self.gpa}"

# apps/results/models.py
# Developed by SAYAB

from django.db import models
from apps.users.models import Student
from apps.courses.models import Course

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.name} - {self.marks_obtained}"

class Transcript(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.created_at}"
