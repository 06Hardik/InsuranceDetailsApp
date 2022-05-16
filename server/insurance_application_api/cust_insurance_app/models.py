from operator import mod
from tkinter import CASCADE
from tkinter.tix import INTEGER
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CustomerDetails(models.Model):
    CustId = models.IntegerField(unique=True)
    Gender= models.CharField(null=True, max_length=10)
    Income_Group = models.CharField(null=True, max_length=500)
    Region = models.CharField(null=True, max_length=100)
    Marital_status = models.BooleanField(blank=True)

    def __str__(self):
        return self.task


class PolicyDetails(models.Model):
    PolicyId = models.IntegerField(unique=True)
    CustId = models.ForeignKey(CustomerDetails,on_delete=models.CASCADE,unique=False)
    Purchase_date = models.DateField(blank = True, editable=False)
    Fuel = models.CharField(null=True, max_length=100)
    VEHICLE_SEGMENT = models.CharField(null=True, max_length=100)
    Premium = models.IntegerField(validators=[MaxValueValidator(1000000), MinValueValidator(0)])
    Bodily_Injury_Liability = models.BooleanField(default = False, blank = True)
    Personal_Injury_Protection = models.BooleanField(default = False, blank = True)
    Property_Damage_Liability = models.BooleanField(default = False, blank = True)
    Collision = models.BooleanField(default = False, blank = True)
    Comprehensive = models.BooleanField(default = False, blank = True)

    def __str__(self):
        return self.task
