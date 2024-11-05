from django.db import models

class Employee_details(models.Model):
    WORK_TYPE_CHOICES = [
        ('contract', 'Contract'),
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
    ]

    employee_id = models.AutoField(primary_key=True) 
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=50)
    experience = models.PositiveIntegerField() 
    department = models.CharField(max_length=50)
    work_type = models.CharField(max_length=30, choices=WORK_TYPE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"


