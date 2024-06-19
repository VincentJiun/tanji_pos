from django.db import models

# Create your models here.
class Foodtype(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Food(models.Model):
    ID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    amount = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    cost_time = models.IntegerField(default=0)
    foodType = models.ForeignKey(
        'Foodtype', to_field="ID", on_delete=models.PROTECT)

    def __str__(self):
        return self.title