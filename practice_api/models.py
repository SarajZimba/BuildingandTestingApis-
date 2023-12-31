from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    company_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices= (('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobile Phones', 'Mobile Phones')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '__' + self.location
    
class Employee(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    employee_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    email = models.CharField(max_length= 200)
    address = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    positon = models.CharField(max_length = 50, choices = (('Junior Backend Developer', 'Junior Backend Developer'), ('Senior Bakend Developer', 'Senior Backend Developer')))

    def __str__(self):
        return self.name
    

