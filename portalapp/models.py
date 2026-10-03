from django.db import models

# Table 1: Student basic info
class Student(models.Model):
    register_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=100)
    college_name = models.CharField(max_length=200)
    semester = models.IntegerField()
    regulation = models.CharField(max_length=10, default='2021')  # e.g. 2017, 2021

    def __str__(self):
        return f"{self.register_number} - {self.name}"


# Table 2: Subject-wise result for a student
class SubjectResult(models.Model):
    GRADE_CHOICES = [
        ('O', 'O - Outstanding'),
        ('A+', 'A+ - Excellent'),
        ('A', 'A - Very Good'),
        ('B+', 'B+ - Good'),
        ('B', 'B - Above Average'),
        ('C', 'C - Average'),
        ('U', 'U - Fail'),
        ('SA', 'SA - Absent'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subjects')
    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=200)
    internal_marks = models.IntegerField()   # max 20
    external_marks = models.IntegerField()   # max 80
    total_marks = models.IntegerField()      # internal + external
    grade = models.CharField(max_length=5, choices=GRADE_CHOICES)
    result = models.CharField(max_length=10, default='Pass')  # Pass / Fail

    def __str__(self):
        return f"{self.student.register_number} - {self.subject_code}"