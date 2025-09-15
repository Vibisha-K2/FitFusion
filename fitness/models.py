from django.db import models

# Create your models here.

class ClassDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Current_weight = models.IntegerField(null=True, blank=True)
    Desired_weight = models.IntegerField(null=True, blank=True)
    Height = models.IntegerField(null=True, blank=True)

class ContactDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)

class SignupDB(models.Model):
    User_name =models.CharField(max_length=100, null=True, blank=True,unique=True)
    Password =models.CharField(max_length=100, null=True, blank=True)
    Confirm_password = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True,blank=True)


class CartDB(models.Model):
    UserName = models.CharField(max_length=50,null=True,blank=True)
    Product_Name = models.CharField(max_length=50,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    TotalPrice = models.IntegerField(null=True,blank=True)
    Product_Image = models.ImageField(max_length=50,null=True,blank=True)

class CheckoutDB(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Place = models.CharField(max_length=50,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    Email = models.EmailField(max_length=50,null=True,blank=True)
    Address = models.CharField(max_length=50,null=True,blank=True)
    Pin_code = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=50,null=True,blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)


