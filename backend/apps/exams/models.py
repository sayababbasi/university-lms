# # # apps/exams/models.py
# # # Developed by SAYAB

# # from django.db import models
# # from apps.courses.models import Course
# # from apps.users.models import Student, Teacher

# # class Exam(models.Model):
# #     title = models.CharField(max_length=255)
# #     course = models.ForeignKey(Course, on_delete=models.CASCADE)
# #     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
# #     date = models.DateTimeField()

# #     def __str__(self):
# #         return self.title

# # class Question(models.Model):
# #     exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
# #     text = models.TextField()
# #     marks = models.FloatField(default=1)

# #     def __str__(self):
# #         return f"{self.exam.title} - {self.text[:50]}"

# # class ExamResult(models.Model):
# #     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
# #     student = models.ForeignKey(Student, on_delete=models.CASCADE)
# #     marks_obtained = models.FloatField()
# #     total_marks = models.FloatField()

# #     def __str__(self):
# #         return f"{self.student.user.username} - {self.exam.title}"


# # apps/exams/models.py
# # Developed by SAYAB

# from django.db import models
# from apps.users.models import Student, Teacher
# from apps.courses.models import Course

# class Exam(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     date = models.DateField()
#     duration_minutes = models.PositiveIntegerField()
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

# class Question(models.Model):
#     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
#     text = models.TextField()
#     max_marks = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return f"{self.exam.title} - Q{self.id}"

# class ExamResult(models.Model):
#     exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     score = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return f"{self.student.user.username} - {self.exam.title} - {self.score}"

# apps/exams/models.py
# Developed by SAYAB

from django.db import models
from apps.courses.models import Course

class Exam(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=50, choices=[("MCQ","MCQ"),("Essay","Essay")])

    def __str__(self):
        return self.text
