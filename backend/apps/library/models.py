# # apps/library/models.py
# # Developed by SAYAB

# from django.db import models
# from apps.users.models import Student, Teacher

# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.CharField(max_length=255)
#     isbn = models.CharField(max_length=50, unique=True)
#     total_copies = models.IntegerField(default=1)
#     available_copies = models.IntegerField(default=1)

#     def __str__(self):
#         return self.title

# class Borrow(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
#     teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
#     borrowed_at = models.DateTimeField(auto_now_add=True)
#     returned_at = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         user = self.student or self.teacher
#         return f"{user.user.username if user else 'Unknown'} - {self.book.title}"


# backend/apps/library/models.py
# Developed by SAYAB

from django.db import models
from django.conf import settings

class Book(models.Model):
    """
    Model representing a book in the library.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    copies_available = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Issue(models.Model):
    """
    Model representing a book issue to a student/staff.
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='issues')
    issued_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned = models.BooleanField(default=False)

    class Meta:
        ordering = ['-issue_date']

    def __str__(self):
        return f"{self.book.title} → {self.issued_to.username}"


class Return(models.Model):
    """
    Model representing the return of a book.
    """
    issue = models.OneToOneField(Issue, on_delete=models.CASCADE, related_name='return_record')
    return_date = models.DateField(auto_now_add=True)
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Return of {self.issue.book.title} by {self.issue.issued_to.username}"
