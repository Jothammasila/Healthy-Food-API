from django.db import models


class Food(models.Model):
    Food_Name = models.CharField(max_length=150)
    Glycemic_Index = models.FloatField(max_length=4)
    Calories = models.FloatField(max_length=3)
    Carbohydrates = models.FloatField(max_length=5)
    Protein = models.FloatField(max_length=3)
    Fat = models.FloatField(max_length=3)
    Suitable_for_Diabetes = models.FloatField(max_length=3)
    Suitable_for_Blood_Pressure = models.FloatField(max_length=3)
    Sodium_Content = models.FloatField(max_length=3)
    Potassium_Content = models.FloatField(max_length=5)
    Magnesium_Content = models.FloatField(max_length=4)
    Calcium_Content = models.FloatField(max_length=4)
    Fiber_Content = models.FloatField(max_length=3)
    
    
    def __str__(self) -> str:
        return f"{self.Food_Name} diet."