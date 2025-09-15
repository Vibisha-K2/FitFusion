from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from fitness.models import SignupDB

# Create your models here.

class Days(models.Model):
    choose = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.choose

# class Interval(models.Model):
#     shift = models.CharField(max_length=100,null=True,blank=True)
#
#     def __str__(self):
#         return self.shift

class Interval(models.Model):
    shift = models.CharField(max_length=100, null=True, blank=True)
    Cat_image = models.ImageField(upload_to="category image",null=True, blank=True)

    def __str__(self):
        return self.shift if self.shift else "Unnamed Interval"


class FoodItems(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    day = models.ForeignKey(Days, on_delete=models.CASCADE,null=True,blank=True)
    interval = models.ForeignKey(Interval, on_delete=models.CASCADE, null=True, blank=True)
    calories =models.IntegerField(null=True,blank=True)
    protein = models.TextField(null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to="food image",null=True, blank=True)

    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    fitname = models.CharField(max_length=100,null=True,blank=True)
    type = models.CharField(max_length=100,null=True,blank=True)
    calories_burned= models.IntegerField(null=True,blank=True)
    Description = models.CharField(max_length=1000,null=True,blank=True)
    image = models.ImageField(upload_to="workout_image", null=True, blank=True)
    video = models.FileField(upload_to="workout",null=True, blank=True)
    created_at = models.DateField(default=datetime.now(),null=True,blank=True)

class ProductDB(models.Model):
    Product_Name=models.CharField(max_length=100, null=True, blank=True)
    calories_burned= models.IntegerField(null=True,blank=True)
    Description=models.CharField(max_length=1000, null=True, blank=True)
    Price=models.IntegerField(null=True, blank=True)
    Category = models.CharField(max_length=50, choices=[('Supplements', 'Supplements'), ('Medications', 'Medications')], null=True, blank=True)
    Product_Image=models.ImageField(upload_to="Pro_image",null=True,blank=True)

class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    total_calories = models.IntegerField()
    created_at = models.DateField(default=datetime.now())
    end_at = models.DateField()

class WorkoutPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    total_duration = models.CharField(max_length=100)
    created_at = models.DateField(default=datetime.now())


class WeightDB(models.Model):
    Weight=models.CharField(max_length=100,null=True,blank=True)
    weight_Description = models.TextField(null=True, blank=True)
    weight_image = models.ImageField(upload_to="weight_image", null=True, blank=True)
    weight_video = models.FileField(upload_to="weight", null=True, blank=True)
    weight_calories = models.CharField(max_length=100,null=True,blank=True)

















class FavoriteSong(models.Model):
    user = models.ForeignKey(SignupDB, on_delete=models.CASCADE)
    song = models.ForeignKey(ProductDB, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'song')

    def __str__(self):
        return f"{self.user.User_name} - {self.song.Product_Name}"