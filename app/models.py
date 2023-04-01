from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_name=models.CharField(max_length=100,primary_key=True)
    dept_no=models.IntegerField(unique=True)
    dept_loc=models.CharField(max_length=100)
    def __str__(self):
        return self.dept_name
class Emp(models.Model):
    emp_no=models.IntegerField(unique=True)
    emp_name=models.CharField(max_length=122,primary_key=True)
    dept_no=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.emp_name
class Family(models.Model):
    f_no=models.IntegerField()
    emp_name=models.ForeignKey(Emp,on_delete=models.CASCADE)
    def __str__(self):
        return self.emp_name