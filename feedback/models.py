from django.db import models
from django.contrib.auth.models import User

class Designation(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee_profile")
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} ({self.designation.name if self.designation else 'No Designation'})"


class FeedbackQuestion(models.Model):
    FEEDBACK_TYPES = [
        ('employee', 'Employee'),
        ('trainer', 'Trainer'),
    ]
    question_text = models.CharField(max_length=255)
    feedback_type = models.CharField(max_length=10, choices=FEEDBACK_TYPES)

    def __str__(self):
        return f"{self.feedback_type} - {self.question_text}"


class FeedbackSubmission(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="feedback_submissions")
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.submitted_by.username} for {self.designation.name}"


class FeedbackAnswer(models.Model):
    submission = models.ForeignKey(FeedbackSubmission, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(FeedbackQuestion, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Answer to {self.question.question_text}"
