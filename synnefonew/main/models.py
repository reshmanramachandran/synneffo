from django.db import models

# Create your models here.
class department(models.Model):
    dep_name=models.CharField(max_length=50)
    def __str__(self):
        return self.dep_name
    
class batch(models.Model):
    batch_time=models.CharField(max_length=50)
    def __str__(self):
        return self.batch_time  


class student(models.Model):
    std_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    dept=models.ForeignKey(department,default=1,on_delete=models.CASCADE)

