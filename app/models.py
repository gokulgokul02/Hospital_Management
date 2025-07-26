from django.db import models

# Create your models here.
class Book(models.Model):
    patient_name=models.CharField(max_length=50)
    patient_age=models.IntegerField(max_length=50)
    patient_phone=models.IntegerField(max_length=15)
    patient_email=models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.patient_name
    
class Admin(models.Model):
    token_no = models.IntegerField(primary_key=True)
    date = models.DateField(max_length=50)
    time = models.TimeField(max_length=50)
    def __str__(self):
     return str(self.token_no)

