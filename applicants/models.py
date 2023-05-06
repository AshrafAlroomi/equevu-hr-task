from django.db import models
from django.core.validators import FileExtensionValidator
from datetime import date


class Department(models.Model):
    DEPARTMENT_CHOICES = [
        ('IT', 'Information Technology'),
        ('HR', 'Human Resources'),
        ('FIN', 'Finance'),
    ]

    code = models.CharField(max_length=3, choices=DEPARTMENT_CHOICES, unique=True)

    def __str__(self):
        return f"<{self.code}: {self.name}>"

    @property
    def name(self):
        for code, name in self.DEPARTMENT_CHOICES:
            if code == self.code:
                return name
        return None


class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    start_working_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/',
                              validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<{self.first_name} {self.last_name}>"

    @property
    def years_of_experience(self):
        today = date.today()
        delta = today - self.start_working_date
        years_of_experience = delta.days // 365
        return years_of_experience
