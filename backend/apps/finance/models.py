# # # apps/finance/models.py
# # # Developed by SAYAB

# # from django.db import models
# # from apps.users.models import Student

# # class FeeChallan(models.Model):
# #     student = models.ForeignKey(Student, on_delete=models.CASCADE)
# #     amount = models.DecimalField(max_digits=10, decimal_places=2)
# #     due_date = models.DateField()
# #     is_paid = models.BooleanField(default=False)
# #     created_at = models.DateTimeField(auto_now_add=True)

# #     def __str__(self):
# #         return f"{self.student.user.username} - {self.amount} Challan"

# # class Payment(models.Model):
# #     student = models.ForeignKey(Student, on_delete=models.CASCADE)
# #     challan = models.ForeignKey(FeeChallan, on_delete=models.CASCADE)
# #     paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
# #     payment_date = models.DateField(auto_now_add=True)
# #     payment_method = models.CharField(max_length=50)

# #     def __str__(self):
# #         return f"{self.student.user.username} - {self.paid_amount} Paid"

# # class Scholarship(models.Model):
# #     student = models.ForeignKey(Student, on_delete=models.CASCADE)
# #     title = models.CharField(max_length=100)
# #     amount = models.DecimalField(max_digits=10, decimal_places=2)
# #     awarded_date = models.DateField(auto_now_add=True)

# #     def __str__(self):
# #         return f"{self.student.user.username} - {self.title}"

# # apps/finance/admin.py
# # Developed by SAYAB

# from django.contrib import admin
# from .models import FeeChallan, Payment, Scholarship

# @admin.register(FeeChallan)
# class FeeChallanAdmin(admin.ModelAdmin):
#     list_display = ("student", "amount_due", "due_date", "status")  # ensure these fields exist
#     list_filter = ("status", "due_date")

# @admin.register(Payment)
# class PaymentAdmin(admin.ModelAdmin):
#     list_display = ("student", "amount_paid", "paid_on", "payment_method")  # ensure fields match
#     list_filter = ("payment_method",)

# @admin.register(Scholarship)
# class ScholarshipAdmin(admin.ModelAdmin):
#     list_display = ("student", "name", "scholarship_type", "amount")  # ensure fields exist
#     list_filter = ("scholarship_type",)


# apps/finance/models.py
# Developed by SAYAB

from django.db import models
from apps.users.models import Student

class FeeChallan(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=50, choices=[("Paid","Paid"),("Unpaid","Unpaid")])

    def __str__(self):
        return f"{self.student.user.username} - {self.amount_due}"

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    paid_on = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=[("Cash","Cash"),("Card","Card"),("Online","Online")])

    def __str__(self):
        return f"{self.student.user.username} - {self.amount_paid}"

class Scholarship(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    scholarship_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.student.user.username}"
