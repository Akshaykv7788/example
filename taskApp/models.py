from django.db import models

# Create your models here.

class Department(models.Model):
    department_id=models.IntegerField(primary_key=True)
    department_name=models.CharField(max_length=100)

    def __str__(self):
        return self.department_name


class EmployDetails(models.Model):
    employ_name=models.CharField(max_length=100)
    employ_number=models.CharField(max_length=10)
    employ_department=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.employ_name

