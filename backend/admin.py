from django.contrib import admin
from .models import *
# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ["name"]

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ["name"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]

class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ["name"]


class MealPlanAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(FoodItems, FoodAdmin)
admin.site.register(Workout, WorkoutAdmin)
admin.site.register(WorkoutPlan, WorkoutPlanAdmin)
admin.site.register(MealPlan, MealPlanAdmin)
admin.site.register(Days)
admin.site.register(Interval)
admin.site.register(ProductDB)
